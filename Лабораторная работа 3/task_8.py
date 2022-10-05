money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05


def how_many_months(capital, sal, sp, incr=increase):
    count = 0
    summ = capital + sal
    while summ > 0:
        summ -= sp
        sp *= (1 + incr)
        count += 1
    return count


# TODO Оформить решение
month = how_many_months(money_capital, salary, spend)  # количество месяцев, которое можно прожить
print(month)
