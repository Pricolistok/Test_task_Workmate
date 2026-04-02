import sys
from src.cli import add_arguments, parse_arguments
from src.report_factory import create_report


def main():
    try:
        parser = add_arguments()
        filenames, report_type = parse_arguments(parser=parser)
        report = create_report(filenames=filenames, report_type=report_type)
        report.print_report()
    except (FileNotFoundError, ValueError) as file_error:
        sys.stderr.write(str(file_error) + '\n')
        sys.exit(1)
    sys.exit(0)


if __name__ == '__main__':
    main()
