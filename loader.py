import csv


def load_data(files: list[str]) -> list[dict]:
    data = []

    for file in files:
        with open(file, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["ctr"] = float(row["ctr"])
                row["retention_rate"] = float(row["retention_rate"])
                data.append(row)

    return data