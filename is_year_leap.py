"""
TASK:
Написать функцию is_year_leap, принимающую 1 аргумент — номер года, и возвращающую True,
если год високосный, и False иначе.
Описание условий посмотрите здесь, раздел: Григорианский календарь.
"""

year_user = int(input('Введите год: '))


def is_year_leap(year):
    if year % 4 == 0 or year % 400 == 0 or year % 100 == 0:  # ПРОВЕРЯЕМ КРАТНОСТЬ НОМЕРА ГОДА
        return True
    else:
        return False


print(is_year_leap(year_user))
