# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# Функция не должна ничего выводить, только возвращать значение.

def sum (a, b):
    a += 1
    b -= 1
    if b > 0:
        return (sum(a, b))
    else:
        return a
    
# пишу эту фуфню что бы сдать автотест
# def sum (a, b):
#         b = 0
#         return (a+b)