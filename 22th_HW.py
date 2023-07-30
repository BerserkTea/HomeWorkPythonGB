# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
from random import randint
# a = {1,4,5,7,1,12,3}
# b = {6,8,4,2,7,9,1,5,6}

a = {randint (-50,50) for _ in range (int(input("Введите длинну первого множества ")))}
b = {randint (-50,50) for _ in range (int(input("Введите длинну второго множества ")))}
print(a)
print(b)
print (sorted(a.union(b)))


# import random
# print(first_set := set([random.randint(0,20) for _ in range(10)]))
# print(second_set := set([random.randint(0,20) for _ in range(10)]))


# print (first_set.intersection(second_set))
# # print([item fo item in first_set if item in second_set])

