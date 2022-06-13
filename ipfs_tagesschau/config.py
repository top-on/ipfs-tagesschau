"""App configuration."""

from urlpath import URL

ARTICLE_BLOCKLIST: list[URL] = [
    URL("https://www.tagesschau.de/multimedia/livestreams/"),
    URL("https://www.tagesschau.de/multimedia/ukrainisch/"),
    URL("https://www.tagesschau.de/multimedia/russisch/"),
]
