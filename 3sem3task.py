# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

# В случае с английским алфавитом очки распределяются так:

# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:

# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

k = 'fable'
# # 12
total=0
price_dict= {
    'AEIOULNSTRАВЕИНОРСТ' : 1,
    'DGДКЛМПУ' : 2,
    'BCMPБГЁЬЯ' : 3,
    'FHVWYЙЫ' : 4,
    'KЖЗХЦЧ' : 5,
    'JXШЭЮ' : 8,
    'QZФЩЪ' :10
    }
new_aplha = {}
for letters, score in price_dict.items():
    new_aplha.update(dict.fromkeys(letters, score))
print (new_aplha)

for char in k.upper():
    total += new_aplha.get(char)

# for i in k.upper():
#     for key in price_dict:
#         if i in key:
#             total+=price_dict[key]
print (total)

# price_dict= {
#     'АВЕИНОРСТ' : 1, 'ДКЛМПУ' : 2, 'БГЁЬЯ' : 3,
#     'ЙЫ' : 4, 'ЖЗХЦЧ' : 5, 'ШЭЮ' : 8, 'ФЩЪ' :10
#     }

# rezult = [key for letter in k for key, value in dict.items() if letter in value]
