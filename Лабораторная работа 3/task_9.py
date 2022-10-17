salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен


def how_much_money(salary, spend, month=months, increase_def=increase):
    money = -10 * salary
    for i in range(month):
        money += spend
        spend *= (1 + increase_def)
    return money


# TODO Оформить решение
need_money = how_much_money(salary, spend)
print(round(need_money))
