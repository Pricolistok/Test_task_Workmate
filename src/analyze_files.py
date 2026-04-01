import csv
from pathlib import Path
from statistics import median
from src.models import SpentStat

def count_median_from_files(data: dict[str, SpentStat], filenames: list[str]) -> None:
    if filenames is None:
        raise 'Haven`t input files'
    for filename in filenames:
        count_median_from_file(data=data, filename=filename)
    sort_data(data=data)
    count_median_from_dict(data=data)


def count_median_from_file(data: dict[str, SpentStat], filename: str) -> None:
    if not Path(filename).exists():
        raise 'File not found'
    with open(filename, encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            name, coffee_spent = row[0], row[2]
            if name not in data:
                data[name] = SpentStat()
            data[name].spent.append(int(coffee_spent))


def count_median_from_dict(data: dict[str, SpentStat]) -> None:
    for key, val in data.items():
        data[key].median = median(val.spent)


def sort_data(data: dict[str, SpentStat]) -> None:
    for item in data.values():
        item.spent.sort()
