import csv


def create_report(clean_data: list[tuple[str, float]], report_name: str | None):
    if report_name is None:
        return
    with open(f'{report_name}.csv', mode='w') as file:
        csvwriter = csv.writer(file, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(['student', 'median_coffee'])
        for item in clean_data:
            csvwriter.writerow([item[0], item[1]])
