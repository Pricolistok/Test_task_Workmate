from src.reports_models import type_of_reports, Report


def create_report(filenames: list[str], report_name: str) -> Report:
    report_class = type_of_reports.get(report_name)
    if report_class is None:
        raise ValueError(f'Report with name {report_name} nor found')
    return report_class(filenames=filenames)