import pytest
from src.services.report_service import generate_report


def test_generate_clickbait_report(tmp_path):
    file = tmp_path / "data.csv"

    file.write_text(
        "title,ctr,retention_rate\n"
        "A,20,30\n"
        "B,10,30\n"
    )

    result = generate_report([str(file)], "clickbait")

    assert "A" in result
    assert "B" not in result


def test_unknown_report(tmp_path):
    file = tmp_path / "data.csv"
    file.write_text("title,ctr,retention_rate\nA,20,30\n")

    with pytest.raises(ValueError):
        generate_report([str(file)], "unknown")