# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
n_count = int(input('Введите число до которого считать вам эту вот как её там, а точно, ну вот это вот....  '))
x=0
ext=1
while ext <= n_count:
 print (f'2 в степени {x} равно {ext}')
 x+=1
 ext*=2
print(f"А вот и всё, дальше все числа уже больше введеного вами ранее {n_count}\nИ финальная степень двойки составила {x-1}")