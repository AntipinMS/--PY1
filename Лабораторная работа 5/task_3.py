rom random import randint


def get_unique_list_numbers() -> list[int]:
    list_ = [randint(-10, 10)]
    num = randint(-10, 10)
    if num not in list_ and len(list_) < 15:
        list_.append(num)
    return list_
    # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
