# Calculating the difference between two points in time
# Version 1.1.1, 24.09.2022
# Created by Katiaryna Sibirava
# QA4822 group

moment1 = h1, m1, s1 = (int(input("Input hour: ")),
                        int(input("Input min: ")),
                        int(input("Input sec: ")))
moment2 = h2, m2, s2 = (int(input("Input hour: ")),
                        int(input("Input min: ")),
                        int(input("Input sec: ")))

result = ((h2 - h1) * 3600 + (m2 - m1) * 60 + (s2 - s1))

if (0 < h1 <= 23 and 0 < h1 <= 23
        and 0 <= m1 <= 59 and 0 <= m2 <= 59
        and 0 <= s1 <= 59 and 0 <= s2 <= 59):
    if h2 >= h1 and m2 >= m1 and s2 >= s1:
        print("Time difference is {} seconds".format(result))
    else:
        print("Error invalid data! Moment2 should be >= moment1")
else:
    print("Error invalid data!")
