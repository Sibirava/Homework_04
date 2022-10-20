# Arithmetic Operations Task
# Version 1.1.1, 27.09.2022
# Created by Katiaryna Sibirava
# QA4822 group


a = int(input("Please, input a: "))
b = int(input("Please, input b: "))

print("Result of testing Arithmetic Operations on int data type in Python")

c = a + b
print("Addition result a + b is:{}".format(c))

c = a - b
print("Subtraction result a - b is {}".format(c))

c = b - a
print("Subtraction result b - a is {}".format(c))

c = a * b
print("Multiplication result a * b is {}".format(c))

if a == 0:
    print("Error. Division by zero is impossible")
else:
    print("Division result b / a is {}".format(b / a))

if b == 0:
    print("Error. Division by zero is impossible")
else:
    print("Division result a / b is {}".format(a / b))

if a == 0:
    print("Error. Division by zero is impossible")
else:
    print("Floor division result b // a is {}".format(b // a))

if b == 0:
    print("Error. Division by zero is impossible")
else:
    print("Floor division result a // b is {}".format(a // b))

if a == 0:
    print("Error. Division by zero is impossible")
else:
    print("Modulus result b % a is {}".format(b % a))

if b == 0:
    print("Error. Division by zero is impossible")
else:
    print("Modulus result a % b is {}".format(a % b))

c = a ** b
print("Exponential result a ** b is {}".format(c))

c = b ** a
print("Exponential result b ** a is {}".format(c))




print("Result of testing Arithmetic Operations on bool data type in Python")
a = bool(input("Please input a =  "))
b = bool(input("Please input b =  "))

c = a + b
print("Addition result a + b is:{}".format(c))

c = a - b
print("Subtraction result a - b is {}".format(c))

c = b - a
print("Subtraction result b - a is {}".format(c))

c = a * b
print("Multiplication result a * b is {}".format(c))

if a == False:
    print("Error. Division by zero is impossible")
else:
    print("Division result b / a is {}".format(b / a))

if b == False:
    print("Error. Division by zero is impossible")
else:
    print("Division result a / b is {}".format(a / b))


if a == False:
    print("Error. Division by zero is impossible")
else:
    print("Floor division result b // a is {}".format(b // a))

if b == False:
    print("Error. Division by zero is impossible")
else:
    print("Floor division result a // b is {}".format( a // b))

if a == False:
    print("Error. Division by zero is impossible")
else:
    print("Modulus result b % a is {}".format(b % a))

if b == False:
    print("Error. Division by zero is impossible")
else:
    print("Modulus result a % b is {}".format(a % b))

c = a ** b
print("Exponential result a ** b is {}".format(c))

c = b ** a
print("Exponential result b ** a is {}".format(c))



print("Result of testing Arithmetic Operations on float data type in Python")
a = float(input("Please, input a: "))
b = float(input("Please, input b: "))

c = round(a + b, 2)
print("Addition result a + b is:{}".format(c))

c = round(a - b, 2)
print("Subtraction result a - b is {}".format(c))

c = round(b - a, 2)
print("Subtraction result b - a is {}".format(c))

c = round(a * b, 2)
print("Multiplication result a * b is {}".format(c))

if a == 0:
    print("Error. Division by zero is impossible")
else:
    print("Division result b / a is {}".format(round(b / a)))


if b == 0:
    print("Error. Division by zero is impossible")
else:
    print("Division result a / b is {}".format(round(a / b, 2)))

if a == 0:
    print("Error. Division by zero is impossible")
else:
    print("Floor division result b // a is {}".format(round(b // a, 2)))

if b == 0:
    print("Error. Division by zero is impossible")
else:
    print("Floor division result a // b is {}".format(round(a // b, 2)))

if a == 0:
    print("Error. Division by zero is impossible")
else:
    print("Modulus result b % a is {}".format(round(b % a, 2)))

if b == 0:
    print("Error. Division by zero is impossible")
else:
    print("Modulus result a % b is {}".format(round(a % b)))

c = round(a ** b, 2)
print("Exponential result a ** b is {}".format(c))

c = round(b ** a, 2)
print("Exponential result b ** a is {}".format(c))
