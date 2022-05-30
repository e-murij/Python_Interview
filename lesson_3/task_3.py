"""
Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения.
Необходимо написать функцию, создающую из данных ключей и значений словарь.
Если ключу не хватает значения, в словаре для него должно сохраняться значение None.
Если есть  значения, которым не хватило ключей, их необходимо отбросить
"""
from itertools import zip_longest


def create_list_key_value(qt_keys, qt_values):
    key_list = [f'key_{i + 1}' for i in range(qt_keys)]
    value_list = [f'value_{i + 1}' for i in range(qt_values)]
    return key_list, value_list


def create_dict(keys, values):
    if len(keys) < len(values):
        return dict(zip(keys, values))
    else:
        return dict(zip_longest(keys, values))


def create_dict_2(keys, values):
    new_dict = {}
    for i, key in enumerate(keys):
        try:
            new_dict[key] = values[i]
        except IndexError:
            new_dict[key] = None
    return new_dict


if __name__ == "__main__":
    print('keys = values')
    keys, values = create_list_key_value(4, 4)
    print(create_dict(keys, values))
    print(create_dict_2(keys, values))

    print('keys > values')
    keys, values = create_list_key_value(6, 4)
    print(create_dict(keys, values))
    print(create_dict_2(keys, values))

    print('keys < values')
    keys, values = create_list_key_value(4, 6)
    print(create_dict(keys, values))
    print(create_dict_2(keys, values))
