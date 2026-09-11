import argparse
import logging

from . import config, db, csv_io
from . import add as add_module
from .filters import Filters, matches
from .scrapers.linkedin_scraper import LinkedInScraper
from .scrapers.glassdoor_scraper import GlassdoorScraper
from .scrapers.discord_scraper import DiscordScraper

log = logging.getLogger(__name__)

SCRAPERS = {
    "linkedin": LinkedInScraper,
    "glassdoor": GlassdoorScraper,
    "discord": DiscordScraper,
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser("job_puller", description="Job application tracker")
    parser.add_argument("--debug", action="store_true", help="Print debug info")
    subparsers = parser.add_subparsers(dest="command")

    scrape = subparsers.add_parser("scrape", help="Scrape job listings from configured sources")
    scrape.add_argument("--source", choices=list(SCRAPERS) + ["all"], default="all")
    scrape.add_argument("--dry-run", action="store_true", help="Fetch and print, but don't write to the database")

    pull = subparsers.add_parser("pull", help="Export the database to a CSV file")
    pull.add_argument("file", help="Path to the output CSV file")
    pull.add_argument("--status", help="Only export jobs with this status")

    sync = subparsers.add_parser("sync", help="Sync a CSV file's changes back into the database")
    sync.add_argument("file", help="Path to the input CSV file")

    add = subparsers.add_parser("add", help="Manually add a job application by URL")
    add.add_argument("url")
    add.add_argument("--title", default="")
    add.add_argument("--company", default="")
    add.add_argument("--location", default="")
    add.add_argument("--job-type", dest="job_type", default="")
    add.add_argument("--discipline", default="")
    add.add_argument("--status", default="to_apply")
    add.add_argument("--notes", default="")

    return parser


def do_scrape(source: str, dry_run: bool):
    filters = Filters.from_dict(config.load_filters())
    sources = SCRAPERS if source == "all" else {source: SCRAPERS[source]}
    total = 0
    for name, scraper_cls in sources.items():
        log.info("Scraping %s...", name)
        jobs = scraper_cls().fetch_listings(filters)
        matched = [j for j in jobs if matches(j, filters)]
        for job in matched:
            if dry_run:
                log.info("[dry-run] %s - %s", job.title, job.url)
            else:
                db.upsert_job(job)
        total += len(matched)
        log.info("%s: %d matching listing(s)", name, len(matched))
    log.info("Scrape complete: %d job(s) %s", total, "would be added (dry-run)" if dry_run else "added/updated")


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    config.setup_logging(args.debug)
    db.init_db()

    if args.debug:
        log.debug("args: %s", args)

    if args.command == "scrape":
        do_scrape(args.source, args.dry_run)
    elif args.command == "pull":
        csv_io.pull_to_csv(args.file, status=args.status)
    elif args.command == "sync":
        csv_io.sync_from_csv(args.file)
    elif args.command == "add":
        add_module.add_by_url(
            args.url, title=args.title, company=args.company, location=args.location,
            job_type=args.job_type, discipline=args.discipline, status=args.status,
            notes=args.notes,
        )
    else:
        parser.print_help()
