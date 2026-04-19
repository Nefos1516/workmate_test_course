from loader import load_data
from src.reports.registry import REPORTS
from src.utils.formatter import format_table


def generate_report(files, report_name):
    if report_name not in REPORTS:
        raise ValueError(f"Unknown report: {report_name}")

    data = load_data(files)

    report = REPORTS[report_name]()
    result = report.generate(data)

    return format_table(result)