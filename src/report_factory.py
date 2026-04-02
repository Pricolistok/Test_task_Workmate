from src.reports import type_of_reports, Report


def check_report_type(report_type: str):
    if type_of_reports.get(report_type) is None:
        raise ValueError(f'Report with type {report_type} not found')


def create_report(filenames: list[str], report_type: str) -> Report:
    check_report_type(report_type=report_type)
    report_class = type_of_reports.get(report_type)
    return report_class(filenames=filenames)
