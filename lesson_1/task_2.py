"""
Реализовать функцию print_directory_contents(path).
Функция принимает имя директории и выводит ее содержимое, включая содержимое всех поддиректории
(рекурсивно вызывая саму себя). Использовать os.walk нельзя, но можно использовать os.listdir и os.path.isfile
"""
import os


def print_directory_contents(path):
    for p in os.listdir(path):
        print(p)
        next_p = os.path.join(path, p)
        if os.path.isdir(next_p):
            print_directory_contents(next_p)


if __name__ == "__main__":
    print_directory_contents(os.path.join(os.getcwd(), os.pardir))
