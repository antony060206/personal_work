import os
import logging
from pathlib import Path
from dotenv import load_dotenv
import yaml

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

DB_PATH = os.environ.get("JOB_PULLER_DB", str(BASE_DIR / "job_applications.db"))
FILTERS_PATH = os.environ.get("JOB_PULLER_FILTERS", str(BASE_DIR / "filters.yaml"))

LINKEDIN_CREDENTIALS = os.environ.get("LINKEDIN_CREDENTIALS")
GLASSDOOR_CREDENTIALS = os.environ.get("GLASSDOOR_CREDENTIALS")
DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

_channel_ids_raw = os.environ.get("DISCORD_CHANNEL_IDS", "")
DISCORD_CHANNEL_IDS = [int(c) for c in _channel_ids_raw.split(",") if c.strip()]


def load_filters() -> dict:
    """Load filter criteria (keywords, locations, job types) from filters.yaml."""
    path = Path(FILTERS_PATH)
    if not path.exists():
        logging.warning("No filters.yaml found at %s, using empty filters", path)
        return {}
    with open(path, "r") as f:
        return yaml.safe_load(f) or {}


def setup_logging(debug: bool = False):
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
