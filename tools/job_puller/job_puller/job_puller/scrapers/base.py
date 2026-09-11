from abc import ABC, abstractmethod
from typing import List

from ..models import JobApplication
from ..filters import Filters


class BaseScraper(ABC):
    """Common interface every site-specific scraper implements."""

    source_name: str = "unknown"

    @abstractmethod
    def fetch_listings(self, filters: Filters) -> List[JobApplication]:
        """Return job postings found from this source (unfiltered is fine;
        the caller applies `filters.matches` before saving)."""
        raise NotImplementedError


class StubScraper(BaseScraper):
    """Base for sources where automated scraping is fragile/against ToS.

    Logs a warning and returns nothing rather than pretending to work.
    """

    def fetch_listings(self, filters: Filters) -> List[JobApplication]:
        import logging
        logging.getLogger(__name__).warning(
            "%s scraper is a stub - see the module docstring for options.",
            self.source_name,
        )
        return []
