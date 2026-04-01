from tabulate import tabulate

def print_report(clean_data: list[tuple[str, float]]):
    print(tabulate(clean_data, headers=['student', 'median_coffee'], tablefmt='grid'))