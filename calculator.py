def main():
    print("Hello! This is a simple pithon calculator")
    while True:
        print("Please,choose a math action: \n"
              "Addition: + \n"
              "Subtraction: - \n"
              "Multiplication: * \n"
              "Division: / \n"
              "Exit: 0 \n")
        action = input("Action: ")
        if action == 0:
            print("Exit program")
            break
        if action in ('+', '-', '*', '/'):
            x = float(input("x = "))
            y = float(input("y = "))
            if action == '+':
                print("{} + {} = {}".format(x, y, x + y))
            elif action == '-':
                print("{} + {} = {}".format(x, y, x - y))
            elif action == '*':
                print("{} + {} = {}".format(x, y, x * y))
            elif action == '/':
                if y != 0:
                    print("{} + {} = {}".format(x, y, x / y))
                else:
                    print("You can't divide into 0. Enter correct number!")
    return

main()