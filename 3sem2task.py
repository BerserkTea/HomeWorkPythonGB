# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

# Пример:


# list_1 = [1, 2, 3, 4, 5]
# k = 6
# # # 5
# number = 0
# for i in range(len(list_1)):
#     if k-list_1[i]<k-number and k-list_1[i]>0:
#         number=i
# print(list_1[number])


# list_1 = [2, 4, 1, 6, 8, 2, 9, 3, 2, 5]
# k = 10

# list_1 = [1, 4, 3, 7, 8, 9, 2]
# k = 8

# list_1 = [1, 12, 6, 7, 8, 15]
# k = 11


k = 10
list_1 = (2, 4, 1, 6, 8, 2, 9, 3, 2, 5)
x = int(input())
print(min(list_1, key=lambda a:abs(a-k)))



list_1 = [1, 2, 3, 4, 5]
k = 6
res = 0
list_2 = []
print (list_1)
for i in range(len(list_1)):
    list_2.append (abs (list_1[i] - k))
for i in range(len(list_2)):
    if min(list_2) == list_2[i]:
        res = i
print (list_1[res])
