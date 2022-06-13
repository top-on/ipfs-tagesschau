"""Functions to render HTML from Jinja templates."""

from jinja2 import Environment, PackageLoader

from ipfs_tagesschau.schema import Article, ArticleSummary


def render_article(article: Article) -> str:

    env = Environment(loader=PackageLoader("ipfs_tagesschau", "templates"))
    template = env.get_template("article.html")

    rendering = template.render(
        title="tagesschau.de",
        heading=article.heading,
        time=article.time,
        text=article.text_blocks,
    )
    return rendering


def render_feed(articles: list[ArticleSummary]) -> str:

    # load template
    env = Environment(loader=PackageLoader("ipfs_tagesschau", "templates"))
    template = env.get_template("index.html")

    rendering = template.render(
        title="tagesschau.de",
        articles=articles,
    )
    return rendering
