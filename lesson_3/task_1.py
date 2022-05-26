"""
Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться путь и имя файла с расширением.
В функции необходимо реализовать поиск имени файла (с расширением),
а затем «выделение» имени файла (без расширения). Расширений может быть несколько (например testfile.tar.gz).

"""
import os


def filename_from_path(path):
    full_filename = os.path.basename(path)
    index = full_filename.index('.')
    filename = full_filename[:index]
    return full_filename, filename


if __name__ == "__main__":
    print(filename_from_path(os.path.abspath(__file__)))
    print(filename_from_path('C:/Users/User/Desktop/Python_Interview/lesson_3/task_1.py.org'))
