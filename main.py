from src.processing_arguments import add_arguments, parse_arguments
from src.utils import create_report


def main():
    add_arguments()
    filenames, report_name = parse_arguments()
    median_stat = create_report(filenames=filenames, report_name=report_name)
    median_stat.print_report()


if __name__ == '__main__':
    main()
