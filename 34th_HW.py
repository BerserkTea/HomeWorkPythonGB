# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам

# poem_to_analise = "пара-ра-рам рам-пам-папам па-ра-па-да"
poem_to_analise = input('Введите стихотворение для анализа ').split()
vowels = "аяуюоеёэиы"
# vowels_lst = ('а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы')
spisok_vhoshdeniy = []
for i in vowels:
    counter = 0
    for j in range(len(poem_to_analise)) :
        if i in list(poem_to_analise[j]):
            spisok_vhoshdeniy.append(list(poem_to_analise[j]).count(i))
if len(set(spisok_vhoshdeniy)) <=1:
    print ('Парам пам-пам')
else:('Пам парам')

# price_dict= {
#     'а' : 1,
#     'я' : 1,
#     'у' : 1,
#     'о' : 1,
#     'ю' : 1,
#     'е' : 1,
#     'ё' : 1,
#     'э' : 1,
#     'и' : 1,
#     'ы' : 1,
#     }
# for i in range(len(poem_to_analise)):
#     counter = 0
#     # print(list(poem_to_analise[i]))
#     for j in vowels_lst:
#         if j in list(poem_to_analise[i]):
#             counter += 0
#     spisok_vhoshdeniy.append(counter)
# print(spisok_vhoshdeniy)

# for i in range(len(poem_to_analise)):
#     start = -1
#     count = 0
#     while True:
#         start = poem_to_analise[i].find("а", start+1)
#         if start == -1:
#             break
#         count += 1

#     print("Количество вхождений символа в строку: ", count )
