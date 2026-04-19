from .base import BaseReport


class ClickbaitReport(BaseReport):
    def generate(self, data):
        filtered = [
            row for row in data
            if row["ctr"] > 15 and row["retention_rate"] < 40
        ]

        return sorted(filtered, key=lambda x: x["ctr"], reverse=True)