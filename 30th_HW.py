# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


def arifm_prog (first_element, diff, total_elements):
    prog_list = [first_element]
    for i in range(2,total_elements+1):                     # Я тут просто подогнал, никак не пойму почему с 2 идет, ну вот никак, хоть и вывод верный))) кек
        prog_list.append(first_element+(i-1)*diff)
    print(prog_list)


first = int(input('Введите первый элемент прогрессии '))
differ = int(input('Введите разность прогрессии '))  
total_lenght = int(input('Введите длинну прогрессии '))

arifm_prog(first, differ, total_lenght)
