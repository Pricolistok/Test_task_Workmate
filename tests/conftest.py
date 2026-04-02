import sys
import pytest
from main import main


def main_runner(args: list[str], capsys):
    argv_tmp = sys.argv
    sys.argv = args
    with pytest.raises(SystemExit) as exc:
        main()
    sys.argv = argv_tmp
    captured = capsys.readouterr()
    return exc.value.code, captured.err.strip(), captured.out.strip()
