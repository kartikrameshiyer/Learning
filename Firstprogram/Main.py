import re

print(" My Calculator")

previous = 0
run = True


def calculator():
    global run
    global previous


    if previous == 0:
        equation = input("Enter the Number")

    else:
        equation = input(str(previous))

    if equation == 'quit':

        run = False

    else:

        equation = re.sub("[A-Z a-z : ;!@#$\'\"]", "", equation)

    if previous == 0:

        previous = eval(equation)
    else:

        previous = eval(str(previous)+ equation)


while run:
    calculator()
