"""

Усовершенствовать программу «Банковский депозит».
Третьим аргументом в функцию должна передаваться фиксированная ежемесячная сумма пополнения вклада.
Считаем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего.
Если 3м аргументом передан 0, то вызов должен быть совпадать с задачей 4.

"""
from lesson_1.task_4 import get_interest_rate, profit_per_month


def bank_deposit_sum(sum_deposit, time_deposit, deposit_add=0):
    interest_rate = get_interest_rate(sum_deposit, time_deposit)
    sum_deposit = sum_deposit + profit_per_month(sum_deposit, interest_rate)
    for month in range(time_deposit - 2):
        interest_rate = get_interest_rate(sum_deposit, time_deposit)
        sum_deposit = sum_deposit + profit_per_month(sum_deposit, interest_rate) + deposit_add
    interest_rate = get_interest_rate(sum_deposit, time_deposit)
    sum_deposit = sum_deposit + profit_per_month(sum_deposit, interest_rate)
    return round(sum_deposit)


if __name__ == "__main__":
    print(bank_deposit_sum(1000, 12, 1000))
