import logging
from datetime import datetime, timezone

import requests
from bs4 import BeautifulSoup

from . import db
from .models import JobApplication

log = logging.getLogger(__name__)


def _guess_title(url: str) -> str:
    """Best-effort page-title guess for a job posting URL. Never fails hard."""
    try:
        resp = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        return soup.title.get_text(strip=True) if soup.title else ""
    except Exception as e:
        log.warning("Could not fetch title for %s: %s", url, e)
        return ""


def add_by_url(url: str, title: str = "", company: str = "", location: str = "",
               job_type: str = "", discipline: str = "", status: str = "to_apply",
               notes: str = "") -> int:
    """Manually add a job application from a URL, filling in a title guess if none given."""
    if not title:
        title = _guess_title(url)
    job = JobApplication(
        source="manual",
        url=url,
        title=title,
        company=company,
        location=location,
        job_type=job_type,
        discipline=discipline,
        date_scraped=datetime.now(timezone.utc).isoformat(),
        status=status,
        notes=notes,
    )
    job_id = db.upsert_job(job)
    log.info("Added/updated job %s (id=%d): %s", url, job_id, title)
    return job_id
