"""
Glassdoor scraper stub - same caveats as linkedin_scraper.py: prefer a manual
export or `job_puller add <url>` over fighting anti-bot measures.
"""
from .base import StubScraper


class GlassdoorScraper(StubScraper):
    source_name = "glassdoor"
