from src.cli import parse_args
from src.services.report_service import generate_report


def main():
    args = parse_args()
    result = generate_report(args.files, args.report)
    print(result)


if __name__ == "__main__":
    main()