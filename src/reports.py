import csv
from pathlib import Path
from statistics import median
from abc import abstractmethod, ABC
from tabulate import tabulate


class Report(ABC):
    def __init__(self, filenames):
        self.filenames: list[str] = filenames
        self.total_stat: dict[str, list[int]] = self.__get_data_from_files()


    def __get_data_from_files(self) -> dict[str, list[int]]:
        total_stat: dict[str, list[int]] = {}
        for filename in self.filenames:
            self.__get_data_from_file(total_stat=total_stat, filename=filename)
        return total_stat


    @staticmethod
    def __get_data_from_file(total_stat: dict[str, list[int]], filename: str) -> None:
        with open(filename, encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                name, coffee_spent = row[0], row[2]
                if name not in total_stat:
                    total_stat[name] = []
                total_stat[name].append(int(coffee_spent))


    @abstractmethod
    def _prepare_data(self):
        pass


    @abstractmethod
    def print_report(self) -> None:
        pass


class MedianCoffee(Report):
    def __init__(self, filenames: list[str]):
        super().__init__(filenames=filenames)
        self.median_stat: list[tuple[str, float]] = self._prepare_data()

    def _prepare_data(self) -> list[tuple[str, float]]:
        result: list[tuple[str, float]] = []
        for key, val in self.total_stat.items():
            result.append((key, median(val)))
        result.sort(key=lambda item: item[1], reverse=True)
        return result

    def print_report(self) -> None:
        print(tabulate(self.median_stat, headers=['student', 'median_coffee'], tablefmt='grid'))


type_of_reports: dict[str, type[Report]] = {
    'median-coffee': MedianCoffee
}