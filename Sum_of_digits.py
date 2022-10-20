#Input the sum of digits task
# Version 1.1.1, 20.09.2022
# Created by Katiaryna Sibirava
# QA4822 group
number = int(input("Input your number: "))

number *= -1 if number < 0 else 1

n1 = number % 10
number = number // 10
n2 = number % 10
number = number // 10
n3 = number % 10
number = number // 10
n4 = number % 10
n5 = number // 10
result = (n1 + n2 + n3 + n4 + n5)
print(result)

#Input the sum of digits task
# Version 1.1.2, 22.09.2022
# Created by Katiaryna Sibirava
# QA4822 group
# def sum_all_number_digits(number):
#     number *= -1 if number < 0 else 1
#     s = 0
#     while number > 0:
#         s += number % 10
#         number //= 10
#     return s
#
#
# def main():
#     number = int(input("Please input your number:  "))
#     s = sum_all_number_digits(number)
#
#     msg = f"Sum of number digits  {number} is {s} "
#     print(msg)
#
# main()
