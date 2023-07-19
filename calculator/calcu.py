def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def checkeven(num1):
    if num1 % 2 == 0 :
        print("The entered number is even")
    else:
        print("The entered number is odd")

def fact(num1):
    if num1 == 1:
        return num1
    else:
        return num1 * fact(num1-1)
    
def fib(terms):
    num1, num2 = 0,1
    i = 0
    while i < terms:
        print(num1)
        num3 = num2 + num1
        num1 = num2
        num2 = num3
        i += 1