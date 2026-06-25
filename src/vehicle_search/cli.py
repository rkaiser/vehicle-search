import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="my-cli",
        description="A simple CLI tool.",
    )

    parser.add_argument(
        "name",
        help="Name to greet.",
    )

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    print(f"Hello, {args.name}!")
