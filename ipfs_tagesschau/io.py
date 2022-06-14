"""Functions for IO."""

import requests
from urlpath import URL


def download_page_source(url: URL) -> str:
    return requests.get(url).text


def save_rendering(rendering: str, filename: str):
    with open(f"build/{filename}", "w") as f:
        f.write(rendering)
