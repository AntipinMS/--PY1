list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_elem = list_numbers.index(max(list_numbers))
list_numbers[max_elem], list_numbers[-1] = list_numbers[-1], list_numbers[max_elem]  # TODO Оформить решение
print(list_numbers)
