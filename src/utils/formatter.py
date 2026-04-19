from tabulate import tabulate


def format_table(data):
    if not data:
        return "No data"

    headers = ["title", "ctr", "retention_rate"]
    rows = [
        [row["title"], row["ctr"], row["retention_rate"]]
        for row in data
    ]

    return tabulate(rows, headers=headers)