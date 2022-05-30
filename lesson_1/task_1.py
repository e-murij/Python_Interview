"""
Вывести таблицу умножения в виде.
1 x 1 = 1
1 x 2 = 2
..
1 x 10 = 10
—
2 x 1 = 2
2 x 2 = 4
…
N x 10 = 10N
Параметр N задается с клавиатуры (или в виде аргумента скрипта, по желанию).
Между разделами вывести разделитель в виде 5 девисов
"""
import sys


def print_multiplication_table(n):
    if n.isdigit() and int(n) <= 10:
        for i in range(1, int(n) + 1):
            for j in range(1, 11):
                print(f"{i} x {j} = {i * j}")
            print('-' * 5)
    else:
        print('Неверно введен параметр n (должно быть целое положительное число от 1 до 10)')


if __name__ == "__main__":
    n = sys.argv[1] if len(sys.argv) > 1 else input('введите n: ')
    print_multiplication_table(n)
