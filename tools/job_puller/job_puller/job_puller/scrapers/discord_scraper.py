"""
Discord scraper: reads recent messages from a job-postings channel your bot
has access to and pulls out any links, so they can be filtered like any
other listing. This uses Discord's own bot API, so it's fine as long as
you're a member of the server / own the bot.

Requires DISCORD_BOT_TOKEN in .env, the "message content" intent enabled on
the bot in the Discord developer portal, and `discord.py` installed.

Standalone test: python -m job_puller.scrapers.discord_scraper <channel_id>
"""
import asyncio
import logging
import re
import sys
from datetime import datetime, timezone
from typing import List, Optional

import discord

from .base import BaseScraper
from ..models import JobApplication
from ..filters import Filters
from .. import config

log = logging.getLogger(__name__)
URL_RE = re.compile(r"https?://\S+")


class DiscordScraper(BaseScraper):
    source_name = "discord"

    def __init__(self, channel_ids: Optional[List[int]] = None, message_limit: int = 200):
        """channel_ids defaults to DISCORD_CHANNEL_IDS from .env (comma-separated),
        so it can be instantiated with no args like the other scrapers."""
        self.channel_ids = channel_ids if channel_ids is not None else config.DISCORD_CHANNEL_IDS
        self.message_limit = message_limit

    def fetch_listings(self, filters: Filters) -> List[JobApplication]:
        return asyncio.run(self._fetch())

    async def _fetch(self) -> List[JobApplication]:
        if not config.DISCORD_BOT_TOKEN:
            log.error("DISCORD_BOT_TOKEN not set in .env")
            return []
        if not self.channel_ids:
            log.error("No Discord channel IDs configured - set DISCORD_CHANNEL_IDS in .env")
            return []

        intents = discord.Intents.default()
        intents.message_content = True
        client = discord.Client(intents=intents)
        results: List[JobApplication] = []

        @client.event
        async def on_ready():
            for channel_id in self.channel_ids:
                channel = client.get_channel(channel_id)
                if channel is None:
                    log.warning("Could not access channel %s (bot not in server, or wrong ID)", channel_id)
                    continue
                async for msg in channel.history(limit=self.message_limit):
                    for url in URL_RE.findall(msg.content):
                        results.append(JobApplication(
                            source=self.source_name,
                            source_id=str(msg.id),
                            url=url,
                            title=msg.content[:200],
                            date_posted=msg.created_at.isoformat(),
                            date_scraped=datetime.now(timezone.utc).isoformat(),
                        ))
            await client.close()

        await client.start(config.DISCORD_BOT_TOKEN)
        return results


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    scraper = DiscordScraper(channel_ids=[int(c) for c in sys.argv[1:]])
    jobs = scraper.fetch_listings(Filters())
    for j in jobs:
        print(j.url, "-", j.title)
