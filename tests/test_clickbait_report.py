import pytest
from src.reports.clickbait import ClickbaitReport


def test_filters_clickbait_videos():
    data = [
        {"title": "A", "ctr": 20, "retention_rate": 30},
        {"title": "B", "ctr": 10, "retention_rate": 30},
        {"title": "C", "ctr": 20, "retention_rate": 50},
    ]

    report = ClickbaitReport()
    result = report.generate(data)

    assert len(result) == 1
    assert result[0]["title"] == "A"


def test_sorting_by_ctr_desc():
    data = [
        {"title": "A", "ctr": 20, "retention_rate": 30},
        {"title": "B", "ctr": 25, "retention_rate": 20},
        {"title": "C", "ctr": 18, "retention_rate": 35},
    ]

    report = ClickbaitReport()
    result = report.generate(data)

    ctrs = [item["ctr"] for item in result]

    assert ctrs == sorted(ctrs, reverse=True)