from src.reports import type_of_reports, Report

def create_report(filenames: list[str], report_type: str) -> Report:
    report_class = type_of_reports.get(report_type)
    if report_class is None:
        raise ValueError(f'Report with type {report_type} not found')
    return report_class(filenames=filenames)
