salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен


def how_much_money(sal, sp, mon=months, incr=increase):
    money = 0
    money -= 10 * sal
    for i in range(mon):
        money += sp
        sp *= (1 + incr)
    return money


# TODO Оформить решение
need_money = how_much_money(salary, spend)
print(round(need_money))
