"""
Инкапсулировать оба параметра (название и цену)
товара родительского класса. Убедиться, что при сохранении текущей логики работы программы будет
сгенерирована ошибка выполнения.
Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
Результат выполнения заданий 1 и 2 должен быть идентичным.

"""


# class ItemDiscount:
#     _name = 'notebook'
#     _price = 200000
#
#
# class ItemDiscountReport(ItemDiscount):
#     def get_parent_data(self):
#         print(f'{super()._name} {super()._price}')


class ItemDiscount:
    __name = 'notebook'
    __price = 200000


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'{super()._ItemDiscount__name} {super()._ItemDiscount__price}')


good_report = ItemDiscountReport()
good_report.get_parent_data()
