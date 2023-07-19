# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть 
from random import randint

uno_count = 0
zero_count = 0
coins = int(input("input, тобишь сюда пиши сколько монеток всего: "))
for _ in range(coins):
    temp = randint(0, 1)
    print (temp, end=" ")
    if temp == 0:
        zero_count+=1
    else:
        uno_count+=1
if zero_count>uno_count:print(f"Необходимо перевернуть {uno_count} монет с решкой")
else: print(f"Необходимо перевернуть {zero_count} монет с орлом")
