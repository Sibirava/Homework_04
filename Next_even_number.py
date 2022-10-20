# Input the next even number task
# Version 1.1.1, 20.09.2022
# Created by Katiaryna Sibirava
# QA4822 group

number = int(input("Input your number: "))

a = number % 2
if a == 1:
    print("Next even number is {}".format(number + 1))
else:
    print("Next even number is {}".format(number + 2))
