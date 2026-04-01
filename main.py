from src.prepare_data import prepare_data
from src.processing_arguments import add_arguments, parse_arguments
from src.analyze_files import count_median_from_files
from src.models import SpentStat
from src.create_report import create_report
from src.print_report import print_report



def main():
    add_arguments()
    filenames, report_name = parse_arguments()
    data: dict[str, SpentStat] = {}
    count_median_from_files(data=data, filenames=filenames)
    clean_data = prepare_data(data=data)
    create_report(clean_data=clean_data, report_name=report_name)
    print_report(clean_data=clean_data)

if __name__ == '__main__':
    main()
