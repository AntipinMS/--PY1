def get_count_char(str_):
    str_ = str_.lower()
    dict_ = {}
    for letter in str_:
        if letter.isalpha() and letter not in dict_:
            dict_[letter] = str_.count(letter)
    return dict_  # TODO посчитать количество каждой буквы в строке в аргументе str_


def frequency(dict_):
    symbols = sum(dict_.values())
    for value in dict_.values():
        value = value / symbols * 100
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(frequency(get_count_char(main_str)))
