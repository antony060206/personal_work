from dataclasses import dataclass, field
from typing import List

from .models import JobApplication


@dataclass
class Filters:
    keywords: List[str] = field(default_factory=list)     # e.g. "electrical engineering"
    disciplines: List[str] = field(default_factory=list)  # e.g. "electrical engineering"
    job_types: List[str] = field(default_factory=list)    # e.g. "intern", "co-op", "student"
    locations: List[str] = field(default_factory=list)    # e.g. "canada"

    @classmethod
    def from_dict(cls, d: dict) -> "Filters":
        return cls(
            keywords=[k.lower() for k in d.get("keywords", [])],
            disciplines=[k.lower() for k in d.get("disciplines", [])],
            job_types=[k.lower() for k in d.get("job_types", [])],
            locations=[k.lower() for k in d.get("locations", [])],
        )


def _any_match(needles: List[str], haystack: str) -> bool:
    haystack = (haystack or "").lower()
    if not needles:
        return True
    return any(n in haystack for n in needles)


def matches(job: JobApplication, filters: Filters) -> bool:
    """Return True if a job listing satisfies ALL active filter categories."""
    text_blob = " ".join([job.title or "", job.discipline or "", job.job_type or ""])
    return (
        _any_match(filters.keywords, text_blob)
        and _any_match(filters.disciplines, job.discipline)
        and _any_match(filters.job_types, job.job_type)
        and _any_match(filters.locations, job.location)
    )
