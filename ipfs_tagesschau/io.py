"""Functions for IO."""

import requests
from urlpath import URL
from pathlib import Path


def download_page_source(url: URL) -> str:
    return requests.get(url).text


def save_rendering(rendering: str, filepath: Path):
    with open(str(filepath), "w") as f:
        f.write(rendering)
