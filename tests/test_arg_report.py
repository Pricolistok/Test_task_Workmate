from tests.conftest import main_runner


def test_report_type_with_error_negative(capsys):
    args = ['main.py', '--files', 'data_in/data_in_1.csv', 'data_in/data_in_2.csv', 'data_in/data_in_3.csv', '--report', 'median-coffffee']
    result_code, std_err_text, std_out_text = main_runner(args=args, capsys=capsys)
    assert result_code == 1
    assert std_err_text  == 'Report with type median-coffffee not found'

def test_empty_report_type_negative(capsys):
    args = ['main.py', '--files', 'data_in/data_in_1.csv', 'data_in/data_in_2.csv', 'data_in/data_in_3.csv', '--report']
    result_code, std_err_text, std_out_text = main_runner(args=args, capsys=capsys)
    assert result_code == 2
    assert 'expected one argument' in std_err_text
