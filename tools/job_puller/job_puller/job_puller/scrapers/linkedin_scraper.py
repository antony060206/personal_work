"""
LinkedIn scraper stub.

LinkedIn's terms discourage automated scraping, and login-walled pages break
often as their markup changes. Rather than fight that, consider one of:

  1. LinkedIn's own "My items > Saved jobs" CSV export, then `job_puller sync`.
  2. A signed-in browser session + a tool you control end-to-end (e.g. a
     browser extension or a script you run manually), at your own risk and
     respecting their terms.
  3. Just pasting individual job URLs with `job_puller add <url>`.

This class is a stub so you can plug in whichever approach you're
comfortable with; it isn't expected to scrape LinkedIn on its own.
"""
from .base import StubScraper


class LinkedInScraper(StubScraper):
    source_name = "linkedin"
