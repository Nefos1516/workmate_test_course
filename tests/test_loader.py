from loader import load_data


def test_load_single_file(tmp_path):
    file = tmp_path / "data.csv"
    file.write_text(
        "title,ctr,retention_rate\n"
        "Video 1,20.5,35\n"
    )

    data = load_data([str(file)])

    assert len(data) == 1
    assert data[0]["title"] == "Video 1"
    assert data[0]["ctr"] == 20.5
    assert data[0]["retention_rate"] == 35.0


def test_load_multiple_files(tmp_path):
    file1 = tmp_path / "data1.csv"
    file2 = tmp_path / "data2.csv"

    file1.write_text("title,ctr,retention_rate\nVideo 1,20,30\n")
    file2.write_text("title,ctr,retention_rate\nVideo 2,25,20\n")

    data = load_data([str(file1), str(file2)])

    assert len(data) == 2