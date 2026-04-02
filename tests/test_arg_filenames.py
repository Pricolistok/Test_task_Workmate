from tests.conftest import main_runner


def test_path_positive(capsys):
    args = ['main.py', '--files', 'data_in/data_in_1.csv', 'data_in/data_in_2.csv', 'data_in/data_in_3.csv', '--report', 'median-coffee']
    result_code, std_err_text, std_out_text = main_runner(args=args, capsys=capsys)
    assert result_code == 0

def test_path_with_error_in_one_arg_negative(capsys):
    args = ['main.py', '--files', 'data_in/data_in_12.csv', 'data_in/data_in_2.csv', 'data_in/data_in_3.csv', '--report', 'median-coffee']
    result_code, std_err_text, std_out_text = main_runner(args=args, capsys=capsys)
    assert result_code == 1
    assert std_err_text == 'File with name data_in/data_in_12.csv not found'

def test_path_with_error_in_more_arg_negative(capsys):
    args = ['main.py', '--files', 'data_in/data_in_12.csv', 'data_in/data_in_21.csv', 'data_in/data_in_3.csv', '--report', 'median-coffee']
    result_code, std_err_text, std_out_text = main_runner(args=args, capsys=capsys)
    assert result_code == 1
    assert std_err_text  == 'File with name data_in/data_in_12.csv not found'

def test_zero_files_args(capsys):
    args = ['main.py', '--files', '--report', 'median-coffee']
    result_code, std_err_text, std_out_text = main_runner(args=args, capsys=capsys)
    assert result_code == 2
    assert 'expected at least one argument' in std_err_text
