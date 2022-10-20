# 1) Определение четности или кратности числа
# number = int(input("Input your number: "))
# result = number % 2 == 0
# print(result)

# 2) Парсинг цифр числа
# number % 5 = 0, 1, 2, 3, 4 , 0 , 1, 2, 3, 4
# ВЫВЕСТИ ПОСЛЕДНЮЮ ЦИФРУ ЧИСЛА
# number = int(input("Input your number: "))
# result = number % 10
# print(result)


# 3) СУММА ЦИФР ЧИСЛА
# number = int(input("Input your number: "))
# n1 = number % 10
# number = number // 10
# n2 = number % 10
# number = number // 10
# n3 = number % 10
# number = number // 10
# n4 = number % 10
# n5 = number // 10
# result = (n1 + n2 + n3 + n4 + n5)
# print(result)

# 4) ДАНО ТРЕХЗНАЧНОЕ ЧИСЛО. ВЫВЕСТИ ПЕРВУЮ ЦИФРУ
# number = int(input("Input your xxx number: "))
# result = number // 100
# if 999 > number > 99:
#     print(result)
# else : print("Error, please input the correct number")


# 5) Дано натуральное число, определите число десятков в нем (предпоследнюю
# цифру числа). Если предпоследней цифры нет, то можно считать, что число
# десятков равно нулю

# number = int(input("Input your number: "))
# number = number //10
# n1 = number % 10
# print(n1)

# 6)На вход даётся натуральное число. Выведите следующее за ним чётное число.
number = int(input("Input your number: "))
a = number % 2
if a == 1:
    print("Next even number is {}". format(number + 1))
else: print("Next even number is {}". format(number + 2))


# 7)Пирожок в столовой стоит A рублей и B копеек. Определите, сколько рублей
# и копеек нужно заплатить за N пирожков.

# price = float(input("Input the price of cake: "))
# a = int(price % 100)
# b = float(round((price - a) * 100))
#
# print("The price of one cake is {} rub and {} coins".format(a, b))
#
# n = int(input("Input the ammount of cakes: "))
# total_cost = float((n * a) + (n * b) / 100)
#
# c = int(total_cost % 100)
# d = float((total_cost - c) * 100)
# # print(c, d)
# print("You have to pay {} rub and {} coins for {}cakes".format(c, d, n))


# Правильное решение
# a = int(input("Input the price of cake rub: "))
# b = int(input("Input the price of cake coins: "))
# n = int(input("Input the amount of cakes: "))
# cost = n * (100 * a + b)
# # print(cost // 100, cost % 100)
# print("You have to pay {} rub and {} coins for {}cakes".format(cost // 100, cost % 100, n))


# 8)Длина Минской кольцевой автомобильной дороги – 56 километров. Байкер
# стартует с нулевого километра МКАД и едет со скоростью V километров в час.
# На какой отметке он остановится через T часов? Программа получает на вход
# целые числа V и T. Если V > 0, то байкер движется в положительном направ-
# лении по МКАД, если же значение V < 0, то в отрицательном. 0 ≤ T ≤ 1000, -
# # 1000 ≤ V ≤ 1000.


# l = 56
# v = int(input("Input biker's speed in km per hour : "))
# t = int(input("Input biker's time in min: "))
# point = ((v * t) % 56)
# print("If biker moves with speed {} km per hour he will be at the point of {} km in {} min".
#       # format(v, point, t))