"""
Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport на два класса.
Инициализировать классы необязательно.
Внутри каждого поместить функцию get_info, которая в первом классе будет отвечать за вывод названия товара,
а вторая — его цены. Далее реализовать вызов каждой из функции get_info.
"""


class ItemDiscount:
    name = 'notebook'
    price = 200000


class ItemDiscountReportName(ItemDiscount):

    def get_info(self):
        print(f'Name: {super().name}')


class ItemDiscountReportPrice(ItemDiscount):

    def get_info(self):
        print(f'Price: {super().price}')


def get_info(obj):
    obj.get_info()


get_info(ItemDiscountReportName())
get_info(ItemDiscountReportPrice())
