from argparse import ArgumentParser
from pathlib import Path


def add_arguments() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("--files", help="Input files", required=True, nargs="+")
    parser.add_argument("--report", help="Type of report", required=True)
    return parser

def parse_arguments(parser: ArgumentParser) -> tuple[list[str], str]:
    args = parser.parse_args()
    check_filenames(filenames=args.files)
    return args.files, args.report

def check_filenames(filenames: list[str]):
    for filename in filenames:
        if not Path(filename).is_file():
            raise FileNotFoundError(f"File with name {filename} not found")
