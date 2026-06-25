from vehicle_search.cli import build_parser


def test_parser_accepts_name() -> None:
    parser = build_parser()
    args = parser.parse_args(["Reid"])

    assert args.name == "Reid"
