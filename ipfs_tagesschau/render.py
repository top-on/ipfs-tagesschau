from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader("ipfs_tagesschau", "templates"))

template = env.get_template("template.html")


content = {
    "title": "tagesschau.de",
    "heading": "artikel 1",
    "timestamp": "timestamp 1",
    "summary": "summary 1",
    "link": "link 1",
}

rendering = template.render(the="variables", **content)

with open("build/index.html", "w") as f:
    f.write(rendering)
