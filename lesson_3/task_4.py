"""
Написать программу, в которой реализовать две функции.
В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение и завершаем работу.
Необходимо открыть файл и создать два списка: с текстовой и числовой информацией.
Для создания списков использовать генераторы.
Применить к спискам функцию zip().
Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение (например example345).
Вызвать вторую функцию. В нее должна передаваться ссылка на созданный файл.
Во второй функции необходимо реализовать открытие файла и простой, построчный вывод содержимого.

"""
import os
import string
from random import randint, choice


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(choice(letters) for i in range(length))
    return rand_string


def create_content_for_file(list_length):
    text_list = [generate_random_string(3) for _ in range(list_length)]
    number_list = [randint(100, 1000) for _ in range(list_length)]
    zip(text_list, map(str, number_list))
    return zip(text_list, map(str, number_list))


def create_and_fill_file(filename, path_to_file=os.getcwd()):
    path = os.path.join(path_to_file, filename)
    if os.path.exists(path):
        print('файл уже существует')
        return
    with open(path, 'w', encoding='UTF-8') as f:
        content = create_content_for_file(list_length=10)
        content_list = [f'{"".join(s)}\n' for s in content]
        f.writelines(content_list)


def print_file_content(filename, path_to_file=os.getcwd()):
    path = os.path.join(path_to_file, filename)
    with open(path, 'r', encoding='UTF-8') as f:
        for line in f:
            print(line, end='')


if __name__ == "__main__":
    create_and_fill_file('file.txt')
    print_file_content('file.txt')
