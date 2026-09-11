import csv
import logging
from dataclasses import asdict, fields
from typing import Optional

from . import db
from .models import JobApplication

log = logging.getLogger(__name__)

FIELDNAMES = [f.name for f in fields(JobApplication)]


def pull_to_csv(path: str, status: Optional[str] = None):
    """Export the database (optionally filtered by status) to a CSV file."""
    jobs = db.fetch_all(status=status)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        for job in jobs:
            writer.writerow(asdict(job))
    log.info("Wrote %d job(s) to %s", len(jobs), path)


def sync_from_csv(path: str):
    """Read a CSV file back into the database, upserting each row by URL.

    Lets you edit statuses/notes in a spreadsheet (e.g. after `pull`) and
    push those edits back into the database.
    """
    count = 0
    with open(path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            clean = {k: (v if v != "" else None) for k, v in row.items() if k in FIELDNAMES}
            if clean.get("id"):
                try:
                    clean["id"] = int(clean["id"])
                except ValueError:
                    clean["id"] = None
            job = JobApplication(**clean)
            db.upsert_job(job)
            count += 1
    log.info("Synced %d row(s) from %s into the database", count, path)
