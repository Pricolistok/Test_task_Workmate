import sys

from src.cli import add_arguments, parse_arguments
from src.report_factory import create_report


def main():
    try:
        filenames, report_type = parse_arguments()
        report = create_report(filenames=filenames, report_type=report_type)
        report.print_report()
    except FileNotFoundError as file_error:
        sys.stderr.write(str(file_error) + '\n')
        sys.exit(1)
    except ValueError as value_error:
        sys.stderr.write(str(value_error) + '\n')
        sys.exit(1)


if __name__ == '__main__':
    add_arguments()
    main()
