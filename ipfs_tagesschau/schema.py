"""Schema models used across this package."""

import bs4
from pydantic import BaseModel
from urlpath import URL


class ArticleSummary(BaseModel):
    heading: str
    url: URL
    link: str
    summary: str

    class Config:
        arbitrary_types_allowed = True


class Article(BaseModel):
    heading: bs4.element.Tag
    time: bs4.element.Tag
    text_blocks: list[bs4.element.Tag]

    class Config:
        arbitrary_types_allowed = True
