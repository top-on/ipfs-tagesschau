"""Scrape ATOM feed of tagesschau.de."""

import requests
import time
from urlpath import URL


from ipfs_tagesschau.parse import parse_article, parse_feed
from ipfs_tagesschau.render import render_article, render_feed
from ipfs_tagesschau.schema import ArticleSummary


# DOWNLOAD FEED
url = URL("https://www.tagesschau.de/xml/atom/")
page_source = requests.get(url).text

# PARSE & RENDER
article_summaries = parse_feed(page_source)
rendering = render_feed(article_summaries)

# SAVE
with open("build/index.html", "w") as f:
    f.write(rendering)


def download_article(article_summary: ArticleSummary):

    page_source = requests.get(article_summary.url).text

    article = parse_article(page_source=page_source)
    rendering = render_article(article=article)

    with open(f"build/{article_summary.url.name}", "w") as f:
        f.write(rendering)


# DOWNLOAD ARTICLES
number_articles = len(article_summaries)
for i, article_summary in enumerate(article_summaries):
    print(
        f"Downloading article {i+1}/{number_articles} ({article_summary.url.name})..."
    )
    download_article(article_summary=article_summary)

    time.sleep(3)
