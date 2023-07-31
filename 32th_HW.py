# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint


n_of_list_1 = int(input('Введите кол-во чисел списка: '))
list_1 = [randint(0,100) for _ in range(n_of_list_1)]
list_dia = input('Введите цифры диапазона для поиска через пробел').split()
print(list_1)
# print (list_dia)

def search_elements (some_array: list,start_num: int, end_num: int):
    # print (len(some_array))
    for i in range(len(some_array)):
        if  start_num<=some_array[i]<=end_num:
            print(f'Номер элемента в списке {i} и сам элемент это {some_array[i]}, он находится в диапазоне между {start_num} и {end_num}.')

search_elements (list_1,int(list_dia[0]), int(list_dia[1]))
            

    