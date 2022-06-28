"""Scrape ATOM feed of tagesschau.de."""

import time
from datetime import datetime
from urlpath import URL
from pytz import timezone

from ipfs_tagesschau.config import OUT_DIR
from ipfs_tagesschau.io import download_page_source, save_rendering
from ipfs_tagesschau.parse import parse_article, parse_feed
from ipfs_tagesschau.render import render_article, render_feed


# CREATE OUTPUT FOLDER
timestamp = datetime.now(tz=timezone("Europe/Berlin")).isoformat()
OUT_DIR.mkdir(exist_ok=True)

# RENDER FEED
page_source = download_page_source(url=URL("https://www.tagesschau.de/xml/atom/"))
summaries = parse_feed(page_source=page_source)
rendering = render_feed(articles=summaries)
save_rendering(rendering=rendering, filepath=OUT_DIR / "index.html")

# DOWNLOAD ARTICLES
for i, article_summary in enumerate(summaries):

    filepath = OUT_DIR / article_summary.url.name

    if filepath.is_file():
        print(f"Skipping article {i+1}/{len(summaries)}. File already exists.")
        continue

    print(f"Loading article {i+1}/{len(summaries)} ({article_summary.url.name})...")

    page_source = download_page_source(url=article_summary.url)
    article = parse_article(page_source=page_source)
    rendering = render_article(article=article)
    save_rendering(rendering=rendering, filepath=filepath)

    time.sleep(3)
