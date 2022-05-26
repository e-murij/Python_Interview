"""
Расширить программу из п. 4:
1.Усовершенствовать первую функцию из предыдущего примера.
Необходимо во втором списке часть строковых значений (выбирается случайно) заменить на значения типа 345example
(в обратном порядке, число и строка).
(То есть вы переделываете функцию записи в файл так, чтобы она иногда меняла запись на 345example)
2.Реализовать функцию поиска определенных подстрок в файле по следующим условиям:
 вывод первого вхождения, вывод всех вхождений.
3.Реализовать функцию замену всех найденных подстрок на новое значение и вывод измененных строк.
 (это ДВЕ ОТДЕЛЬНЫЕ функции которые ВЫВОДЯТ значения, не записывают и не модифицируют файлы)

"""

import os
import string
from random import randint, choice, sample


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(choice(letters) for i in range(length))
    return rand_string


def create_content_for_file(list_length, change_count):
    text_list = [generate_random_string(3) for _ in range(list_length)]
    number_list = [randint(100, 1000) for _ in range(list_length)]
    change_index = sample(range(list_length), change_count)
    for ind in change_index:
        text_list[ind], number_list[ind] = number_list[ind], text_list[ind]
    return zip(map(str, text_list), map(str, number_list))


def create_and_fill_file(filename, path_to_file=os.getcwd()):
    path = os.path.join(path_to_file, filename)
    if os.path.exists(path):
        print('файл уже существует')
        return
    with open(path, 'w', encoding='UTF-8') as f:
        content = create_content_for_file(list_length=10, change_count=4)
        content_list = [f'{"".join(s)}\n' for s in content]
        f.writelines(content_list)


def print_file_content(filename, path_to_file=os.getcwd()):
    path = os.path.join(path_to_file, filename)
    with open(path, 'r', encoding='UTF-8') as f:
        for line in f:
            print(line, end='')


def search_in_file(str_for_search, filename, path_to_file=os.getcwd(), first=False):
    path = os.path.join(path_to_file, filename)
    result = []
    with open(path, 'r', encoding='UTF-8') as f:
        for line in f:
            if str_for_search in line:
                result.append(line)
                if first:
                    return result
        return result


def replace_str(str_for_replace, replaced_by, filename, path_to_file=os.getcwd()):
    path = os.path.join(path_to_file, filename)
    with open(path, 'r', encoding='UTF-8') as f:
        content = f.readlines()
    new_content = [el.replace(str_for_replace, replaced_by) for el in content]
    return new_content


if __name__ == "__main__":
    create_and_fill_file('file.txt')
    print_file_content('file.txt')
    print('Первое вхождение:')
    print(*search_in_file('5', 'file.txt', first=True))
    print('Все вхождения:')
    print(*search_in_file('5', 'file.txt', first=False))
    print('Замена:')
    print(*replace_str(str_for_replace='5', replaced_by='five', filename='file.txt'))
