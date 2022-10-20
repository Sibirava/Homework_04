#ОБМЕН ЗНАЧЕНИЯМИ ПЕРЕМЕННЫХ
#СПОСОБ №1
# a = input("Input a: ")
# b = input("Input b: ")
#
# temp = a
# a = b
# b = temp
#
# print('a = ', a)
# print('b = ', b)

#СПОСОБ№2 Если переменные числовые
# a = int(input("Input a: "))
# b = int(input("Input b: "))
#
# a = a + b
# b = a - b
# a = a - b
#
# print('a = ', a)
# print('b = ', b)


#СПОСОБ№3
a = input("Input a: ")
b = input("Input b: ")

a, b = b, a

print('a = ', a)
print('b = ', b)