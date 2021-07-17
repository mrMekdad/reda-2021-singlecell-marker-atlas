import argparse
from singlecell_marker_atlas.core import build_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Marker reference organizer with metadata validation and export views.")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    if args.summary:
        print(build_snapshot())


if __name__ == "__main__":
    main()
