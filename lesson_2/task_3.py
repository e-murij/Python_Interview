"""
Реализовать возможность переустановки значения цены товара в родительском классе.
Проверить, распечатать информацию о товаре.

"""


class ItemDiscount:
    name = 'notebook'
    price = 200000


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'{super().name} {super().price}')

    def change_price(self, new_price):
        ItemDiscount.price = new_price


good_report = ItemDiscountReport()
good_report.get_parent_data()
good_report.change_price(3000000)
good_report.get_parent_data()
