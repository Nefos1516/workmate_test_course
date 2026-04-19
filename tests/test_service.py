import pytest
from src.utils.formatter import format_table


def test_format_table_with_data():
    data = [
        {"title": "A", "ctr": 20, "retention_rate": 30},
    ]

    table = format_table(data)

    assert "A" in table
    assert "ctr" in table


def test_format_table_empty():
    result = format_table([])

    assert result == "No data"