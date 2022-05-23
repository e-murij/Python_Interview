"""
Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний класс.
Выполнить перегрузку методов конструктора дочернего класса
(метод __init__, в который должна передаваться переменная — скидка)
, и перегрузку метода __str__ дочернего класса. В этом методе должна пересчитываться цена и возвращаться результат
 — цена товара со скидкой. Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы
(вторая и третья строка после объявления дочернего класса).

"""


class ItemDiscount:
    name = 'notebook'
    price = 200000


class ItemDiscountReport(ItemDiscount):

    def __init__(self, discount):
        self.discount = discount

    def get_parent_data(self):
        print(f'{super().name} {super().price}')

    def __str__(self):
        return f'{super().price - self.discount}'


good_report = ItemDiscountReport(1000)
print(good_report)
