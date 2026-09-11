from dataclasses import dataclass
from typing import Optional


@dataclass
class JobApplication:
    id: Optional[int] = None
    source: str = "manual"          # linkedin, glassdoor, discord, manual
    source_id: Optional[str] = None # unique id from the source, used for de-dup
    url: str = ""
    title: str = ""
    company: str = ""
    location: str = ""
    job_type: str = ""              # full-time, internship, co-op, etc.
    discipline: str = ""            # electrical engineering, etc.
    date_posted: Optional[str] = None
    date_scraped: Optional[str] = None
    status: str = "to_apply"        # to_apply, applied, interview, rejected, offer
    date_applied: Optional[str] = None
    notes: str = ""
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
