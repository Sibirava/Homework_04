# Currency Converter
# Version 1.1.1
# Created by Katiaryna Sibirava
# QA4822 group

BYN = input("Please input your number in BYN: ")
BYN = float(BYN)
USD = round(0.3944 * BYN, 2)
EURO = round(0.3946 * BYN, 2)
Zloty = round(1.8687 * BYN, 2)
RUB = round(23.6867 * BYN, 2)
print("Your summ of money {} BYN is \n {} USD,\n {} EURO, \n {} Zloty,\n {} RUB"
      .format(BYN ,USD, EURO, Zloty,RUB))