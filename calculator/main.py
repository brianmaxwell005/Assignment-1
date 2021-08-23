# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
def sum(x , y):
    return 'x' + 'y'

def subtract(x, y):
    return 'x'-'y'

def mult(x, y):
    return 'x' * 'y'

def div(x, y):
    return 'x' / 'y'

    print('1.add')
    print('2.subtract')
    print('3.multiply')
    print('4.div')

    while True:
        choice = input("ENTER CHOICE 1/2/3/4):")
        if choice in ('1','2','3','4'):
            numb1 = float(input('Enter first number:'))
            numb2 = float(input('Enter second number:'))
            if choice == '1':
                print(numb1, "+", numb2, "=", add(numb1,numb2))
            elif choice == '2':
                print(numb1, "-", numb2, "=", subtract(numb1, numb2))
            elif choice == '3':
                print(numb1, "*", numb2, "=", mult(numb1, numb2))
            elif choice == '4':
                print(numb1, "/", numb2, "=", div(numb1, numb2))
            break
        else:
            print('invalid input')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sum(x,y)
    subtract('x,y')
    mult('x,y')
    div('x,y')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
