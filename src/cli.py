from argparse import ArgumentParser
from pathlib import Path

parser = ArgumentParser()

def add_arguments() -> None:
    parser.add_argument("--files", help="Input files", required=True, nargs="+", )
    parser.add_argument("--report", help="Type of report", required=True)


def parse_arguments() -> tuple[list[str] | None, str | None]:
    args = parser.parse_args()
    check_filenames(filenames=args.files)
    return args.files, args.report


def check_filenames(filenames: list[str]):
    for filename in filenames:
        if not Path(filename).exists():
            raise FileNotFoundError(f"File with name {filename} not found")
