# job_puller

```
pip install -r requirements.txt
cp .env.example .env      # fill in DISCORD_BOT_TOKEN etc.

python run.py add https://example.com/job/123 --company "Acme" --title "EE Intern"
python run.py scrape --source discord
python run.py pull applications.csv
# edit applications.csv (e.g. update status column), then:
python run.py sync applications.csv
```

## Sources

- **discord** - live and working. Reads recent messages from one or more
  Discord channels (e.g. a job-postings channel in a server like Northern
  Dev) via a bot, and extracts any links as candidate listings.
  1. Create a bot at https://discord.com/developers/applications, enable the
     "Message Content" intent under Bot settings, and invite it to the
     server with "Read Messages/View Channel" + "Read Message History".
  2. Enable Developer Mode in Discord (Settings > Advanced), right-click the
     channel(s) you want scraped, and "Copy Channel ID".
  3. Set `DISCORD_BOT_TOKEN` and `DISCORD_CHANNEL_IDS` (comma-separated) in `.env`.
- **linkedin** / **glassdoor** - stubs. Both sites actively fight automated
  scraping and/or discourage it in their ToS, so rather than build something
  fragile, these log a warning and return nothing. Prefer a manual CSV
  export from the site (then `job_puller sync`) or `job_puller add <url>`
  for one-off postings.

Filters live in `filters.yaml` and apply to `scrape`. `add` always inserts
regardless of filters, since you're adding it on purpose.

Statuses used in the `status` column: to_apply, applied, interview, rejected, offer.
