"""
    Написать программу «Банковский депозит».
    Клиент банка делает депозит на определенный срок.

    В зависимости от суммы и срока вклада определяется процентная ставка:
    1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 и более года — 5 % годовых).
    10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 и более года – 6.5 % годовых).
    100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 и более года — 7.5 % годовых).

    Проценты начисляются на депозит в конце каждого месяца.

    Необходимо написать функцию, в которую будут передаваться параметры: сумма вклада и срок вклада
    (в месяцах), а на выходе возвращать сумму вклада на конец срока.

"""


def get_interest_rate(sum_deposit, time_deposit):
    if 1000 <= sum_deposit < 10000:
        if 6 <= time_deposit < 12:
            return 0.05
        elif 12 <= time_deposit < 24:
            return 0.06
        elif time_deposit >= 24:
            return 0.05
    elif 10000 <= sum_deposit < 100000:
        if 6 <= time_deposit < 12:
            return 0.06
        elif 12 <= time_deposit < 24:
            return 0.07
        elif time_deposit >= 24:
            return 0.065
    elif 100000 <= sum_deposit < 1000000:
        if 6 <= time_deposit < 12:
            return 0.07
        elif 12 <= time_deposit < 24:
            return 0.08
        elif time_deposit >= 24:
            return 0.075


def profit_per_month(sum_deposit, interest_rate):
    return (sum_deposit * interest_rate) / 12


def bank_deposit_sum(sum_deposit, time_deposit):
    for month in range(time_deposit):
        sum_deposit = sum_deposit + profit_per_month(sum_deposit, get_interest_rate(sum_deposit, time_deposit))
    return round(sum_deposit)


if __name__ == "__main__":
    print(bank_deposit_sum(1000, 12))
