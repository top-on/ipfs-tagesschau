"""Test-Download article text."""

import newspaper
from newspaper import Article

# from newspaper import news_pool

tagesschau_paper = newspaper.build("http://tagesschau.de")
for article in tagesschau_paper.articles:
    print(article.url)


import requests
from newspaper import fulltext

URL = "https://www.tagesschau.de/ausland/europa/spanien-doggy-bags-101.html"

a = Article(url=URL)

a.download()
a.parse()
a.text
