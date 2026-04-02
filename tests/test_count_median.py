from src.reports import MedianCoffee


def test_median_calculation_positive():
    report = MedianCoffee(['data_in/data_in_1.csv', 'data_in/data_in_2.csv', 'data_in/data_in_3.csv'])
    stat = report.get_median_stat()
    expected_stat = [
        ('Иван Кузнецов', 650), ('Олег Морозов', 575.0), ('Алексей Смирнов', 510.0),
        ('Дмитрий Фролов', 495.0), ('Кирилл Андреев', 430), ('Павел Новиков', 420),
        ('Елена Волкова', 310), ('Наталья Орлова', 260), ('Дарья Петрова', 250),
        ('Анна Белова', 230.0), ('Мария Соколова', 125.0)
    ]
    assert expected_stat == stat
