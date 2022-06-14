"""Scrape ATOM feed of tagesschau.de."""

import shutil
import time
from urlpath import URL

from ipfs_tagesschau.config import OUT_DIR
from ipfs_tagesschau.io import download_page_source, save_rendering
from ipfs_tagesschau.parse import parse_article, parse_feed
from ipfs_tagesschau.render import render_article, render_feed


# RESET OUTPUT FOLDER
shutil.rmtree(OUT_DIR)
OUT_DIR.mkdir(exist_ok=True)

# RENDER FEED
page_source = download_page_source(url=URL("https://www.tagesschau.de/xml/atom/"))
summaries = parse_feed(page_source=page_source)
rendering = render_feed(articles=summaries)
save_rendering(rendering=rendering, filename="index.html")

# DOWNLOAD ARTICLES
for i, article_summary in enumerate(summaries):

    print(f"Loading article {i+1}/{len(summaries)} ({article_summary.url.name})...")

    page_source = download_page_source(url=article_summary.url)
    article = parse_article(page_source=page_source)
    rendering = render_article(article=article)
    save_rendering(rendering=rendering, filename=article_summary.url.name)

    time.sleep(3)
