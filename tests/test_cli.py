from src.cli import parse_args


def test_parse_args(monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["prog", "--files", "file1.csv", "file2.csv", "--report", "clickbait"]
    )

    args = parse_args()

    assert args.files == ["file1.csv", "file2.csv"]
    assert args.report == "clickbait"