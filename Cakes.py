#"Input the cost of for n cakes in rub and coins" task
# Version 1.1.1, 22.09.2022
# Created by Katiaryna Sibirava
# QA4822 group

a = int(input("Input the price of cake rub: "))
b = int(input("Input the price of cake coins: "))
n = int(input("Input the amount of cakes: "))
cost = n * (100 * a + b)
print("You have to pay {} rub and {} coins for {}cakes".format(cost // 100, cost % 100, n))
