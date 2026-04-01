from argparse import ArgumentParser

parser = ArgumentParser()

def add_arguments() -> None:
    parser.add_argument("--files", nargs="*", help="Input files")
    parser.add_argument("--report", help="Output file")

def parse_arguments() -> tuple[list[str] | None, str | None]:
    args = parser.parse_args()
    return args.files, args.report
