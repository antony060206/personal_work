import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from typing import List, Optional

from .models import JobApplication
from . import config

SCHEMA = """
CREATE TABLE IF NOT EXISTS job_applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT NOT NULL DEFAULT 'manual',
    source_id TEXT,
    url TEXT NOT NULL,
    title TEXT,
    company TEXT,
    location TEXT,
    job_type TEXT,
    discipline TEXT,
    date_posted TEXT,
    date_scraped TEXT,
    status TEXT NOT NULL DEFAULT 'to_apply',
    date_applied TEXT,
    notes TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    UNIQUE(url)
);
"""


@contextmanager
def get_connection():
    conn = sqlite3.connect(config.DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db():
    with get_connection() as conn:
        conn.execute(SCHEMA)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def upsert_job(job: JobApplication) -> int:
    """Insert a job, or update it if a row with the same URL already exists.

    URL is the de-dup key: re-scraping or re-syncing the same posting updates
    it in place instead of creating a duplicate row.
    """
    now = _now()
    with get_connection() as conn:
        cur = conn.execute("SELECT id FROM job_applications WHERE url = ?", (job.url,))
        existing = cur.fetchone()
        if existing:
            job.id = existing["id"]
            conn.execute(
                """UPDATE job_applications SET
                    source=?, source_id=?, title=?, company=?, location=?, job_type=?,
                    discipline=?, date_posted=?, date_scraped=?, status=?, date_applied=?,
                    notes=?, updated_at=?
                   WHERE id=?""",
                (job.source, job.source_id, job.title, job.company, job.location, job.job_type,
                 job.discipline, job.date_posted, job.date_scraped, job.status, job.date_applied,
                 job.notes, now, job.id),
            )
            return job.id
        cur = conn.execute(
            """INSERT INTO job_applications
               (source, source_id, url, title, company, location, job_type, discipline,
                date_posted, date_scraped, status, date_applied, notes, created_at, updated_at)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (job.source, job.source_id, job.url, job.title, job.company, job.location,
             job.job_type, job.discipline, job.date_posted, job.date_scraped, job.status,
             job.date_applied, job.notes, now, now),
        )
        return cur.lastrowid


def fetch_all(status: Optional[str] = None) -> List[JobApplication]:
    query = "SELECT * FROM job_applications"
    params: tuple = ()
    if status:
        query += " WHERE status = ?"
        params = (status,)
    query += " ORDER BY created_at DESC"
    with get_connection() as conn:
        rows = conn.execute(query, params).fetchall()
    return [JobApplication(**dict(row)) for row in rows]
