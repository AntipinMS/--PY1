money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05


def how_many_months(capital, salary, spend, incr=increase):
    count = 0
    summ = capital + salary
    while summ > 0:
        summ -= spend
        spend *= (1 + incr)
        count += 1
    return count


# TODO Оформить решение
month = how_many_months(money_capital, salary, spend)  # количество месяцев, которое можно прожить
print(month)
