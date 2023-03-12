# Небольшой разбор перебора по словарю
"""
my_dict = {1:'one', 2:'two', 3:'three'}

for key in my_dict: # проход по ключам
    print(key)

for i in my_dict.keys(): # проход по ключам (тоже самое, что и сверху)
    print(i)

for i in my_dict.values(): # проход по знаениям
    print(i)

for i in my_dict.items(): # проход по ключам и значениям (возвращает кортеж - (1, 'one'))
    print(i)

for i, j in my_dict.items(): # проход по ключам и значениям  в развернутом виде (возвращает - 1 one)
    print(i, j)
"""
# Задача: найти значение из словаря, который есть в списке
"""
my_dict = {1:'one', 2:'two', 3:'three'}
my_list = ['three', 'four', 'five']
for i in my_dict.values(): # работаем только со значениями
    if i in my_list:
        print(True)
        break
else:
    print(False)
"""
# Задача: если наоборот нужно найти по значению ключ
"""
my_dict = {1:'one', 2:'two', 3:'three'}
my_list = ['three', 'four', 'five']
for i, v in my_dict.items(): # проходимся по словарю и ищем значение из списка, если находим, то выводим ключ
    if v in my_list:
        print(i)
        break
else:
    print(False)
"""
# Допинформация
"""
my_dict = {1:'one', 2:'two', 3:'three'}
print(my_dict)
my_dict[4] = 'four' # добавление в словарь
my_dict.get(5, 'нету ла') # вызов по ключу, но даже если ент, то не вызовет ошибку
exampe = my_dict.get(5, 'нету ла') # как вариант принта
print(exampe)
print(my_dict) # но в словаре 5-ка не появится
"""

# Продолжение
"""
my_dict = {1:'one', 2:'two', 3:'three'}
print(my_dict)
my_dict.setdefault(5, 'five') # если ключа нет, то он его добавляет с указанным значением
my_dict.setdefault(3, 'five') # если ключ есть, то изменений не поизойдет {1: 'one', 2: 'two', 3: 'three', 5: 'five'}
print(my_dict)
"""
# __________________________
# __________________________

# Task 1
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Например:
# my_list = [1,2,3,4,5,6,5,5,3,6]
# 1, 2, 3, 4, 5, 6, 5_1, 6_1, 5_2, 3_1, 6_1
# Variant 1
"""
import random
my_list = [random.randint(1, 5) for i in range(10)]
print(my_list)
my_dict = {}

for i in my_list:
    my_dict[i] = my_dict.get(i, -1) + 1 # Циклом проходим по списку, и вносим значения в словарь.
                                        # Если значение i впервые встречается, то мы его меняем на -1
                                        # Таким образом, первый раз будет -1+1=0,
                                        # второй раз встречается со значением 0+1=1, потом 1+1=2, 2+1=3 и т.д
    print('\n' + f' {my_dict}') # последовательное заполнение словаря
    print(i if my_dict.get(i) == 0 else f'{i}_{my_dict.get(i)}', end= ',')
print('\n' + f' {my_dict}')
# """

# Variant 2
"""
string = input('Input string: ')
print(string)
dict = {}

for i in string:
    dict[i] = dict.get(i, 0) + 1

    if dict[i] == 1:
        print(i, end=',')
    else:
        print(f'{i}_{dict[i]-1}', end=',' )
"""
# _________________
# _________________
# Task 2

# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.Определите, сколько различных
# слов содержится в этом тексте.
"""
string = 'Пользователь вводит текст (строка). Словом словом текст '
new_str = string.lower().split()
print(new_str)
my_dict = {}
for word in new_str:
    my_dict[word] = my_dict.get(word, 0) + 1
print(my_dict)
count = 0
for i in my_dict.values():
    # if i == 1:
        count+=1
print(count)

key = my_dict.keys()
print(len(key))

print(len(set(new_str)))
"""
# Домашняя задача со 2-го семинара.
# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
"""
sum = int(input('Input sum: '))
mult = int(input('Input multy: '))
x = y = 0
a, b, c = 1, -sum, mult


def roots(a, b, c):
    dicr = b ** 2 - 4 * a * c
    if dicr > 0:
        x1 = (-b - dicr ** 0.5) / 2 * a
        x2 = (-b + dicr ** 0.5) / 2 * a
        return int(x1), int(x2)
    elif dicr == 0:
        x = -b / 2 * a
        return int(x)
    else:
        print('Петя обманул Катю')


print(roots(a, b, c))
"""
# Task 3

# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]
# Variant 1
"""
import random
# Первый этап
my_list = [random.randint(1000, 10000) for i in range(7)]
print(my_list)
# Второй этап
new_list = []
end_list = []
x = input('Input digit: ')
for value in my_list:
    el = str(value)
    if x in el:
        el = el.replace(x, '')
    new_list.append(el)
print(new_list)
# Третий этап
for value in new_list:
    sum_x = sum([(int(el)) for el in value])
    while sum_x > 9:
        sum_x = sum([int(el) for el in str(sum_x)])
    end_list.append(sum_x)
print(end_list)

# Четвертый этап
print(set(end_list))
"""
### Variant 2
import random
# Первый этап
my_list = [str(random.randint(1000, 10000)) for i in range(7)]
print(my_list)
# Второй этап
numToRemove = input('Input number: ')
new_list = []
for i in my_list:
    i = i.replace(numToRemove, "")
    new_list.append(i)
print(new_list)
# Третий этап

def sumOfNum(num):
    sum = 0
    for i in range(len(num)):
        sum += int(num[i])
        if sum < 10:
            return sum
        num = str(sum)
        return sumOfNum(num)

end_list = []
for num in new_list:
    end_list.append(sumOfNum(num))
print(end_list)

# Четвертый этап
setNum = set(end_list)
print(setNum)




