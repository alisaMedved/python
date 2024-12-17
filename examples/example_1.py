
def sum_args(*args):
    summa =0
    for item in args:
        summa = summa + item
    return summa

# импорт сверху

from base.function import upper_and_lower
print(upper_and_lower('fgtrrTwerfv'))
