#THE SQUIRREL TASK
n = ammount_of_squirrels = input("Please input the ammount of squirrels: ")
n = int(n)

k = ammount_of_nuts = input("Please input the ammount of nuts: ")
k = int(k)

result = k // n
result2 = k % n

print ("If {} squirrels divide {} nuts each squirel gets {} nuts. And there will be left {} nut(s)"
       .format(n, k, result, result2))