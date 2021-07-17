"""Core workflow for Single Cell Marker Atlas by Red@."""

PROJECT_NAME = "Single Cell Marker Atlas"
DOMAIN_THEME = "bioinformatics"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": DOMAIN_THEME}
