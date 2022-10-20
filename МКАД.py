# Biker on a ring road task.
# Version 1.1.1, 26.09.2022
# Created by Katiaryna Sibirava
# QA4822 group

l = 56
v = int(input("Input biker's speed in km per hour : "))
t = int(input("Input biker's time in min: "))
point = ((v * t) % 56)
print("If biker moves with speed {} km per hour he will be at the point of {} km in {} min".
      format(v, point, t))
