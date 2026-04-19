import pytest
from loader import load_data


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_data(["nonexistent.csv"])