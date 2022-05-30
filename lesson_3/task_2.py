"""
Написать программу, которая запрашивает у пользователя ввод числа.
На введенное число она отвечает сообщением, целое оно или дробное.
Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
Если они совпадают, программа должна возвращать значение True, иначе False.

"""


def number_check(number):
    if number.isnumeric():
        return f'Число {number} целое'
    try:
        float(number)
        index = number.index('.')
        flag = (number[:index] == number[-index:])
        print(f'Число {number} дробное.')
        return flag
    except ValueError:
        return f'{number} не число'


if __name__ == "__main__":
    print(number_check(input('Number: ')))
