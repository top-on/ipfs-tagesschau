"""Parse page source to structured data, used for rendering."""

from bs4 import BeautifulSoup
from urlpath import URL

from ipfs_tagesschau.schema import Article, ArticleSummary


def parse_article(page_source: str) -> Article:

    soup = BeautifulSoup(page_source, "html.parser")

    heading = soup.find("span", {"class": "seitenkopf__headline--text"})
    time = soup.find("div", {"class": "metatextline"})
    text_blocks = soup.select("p.textabsatz, h2.meldung__subhead")

    article = Article(
        heading=heading,
        time=time,
        text_blocks=text_blocks,
    )
    return article


def parse_feed(page_source: str) -> list[ArticleSummary]:

    soup = BeautifulSoup(page_source, "lxml")
    articles_raw = soup.findAll("entry")

    articles_dict = [
        {
            "heading": entry.title.text,
            "url": URL(entry.link.get("href")),
            "link": URL(entry.link.get("href")).name,
            "summary": entry.summary.text,
        }
        for entry in articles_raw
    ]

    articles = [ArticleSummary(**article) for article in articles_dict]

    articles_filtered = [
        article
        for article in articles
        if (
            str(article.url).endswith(".html")
            and str(article.url).startswith("https://www.tagesschau.de")
        )
    ]

    return articles_filtered
