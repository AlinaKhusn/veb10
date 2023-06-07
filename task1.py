# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv


import random, string

#здесь пишем код

def generate_random_name():

        for k in iter(int, 1):
            x = ''
            n = random.randint(1, 15)
            for i in range(n):
                z =chr(random.randint(97, 122))
                x += z
            x += ' ' + x
            yield x


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))