from calcu import *
answer1 = input("hello, do you want to start (yes): ")
answer2 =['add', 'sub', 'multiply', 'divide','checkeven', 'fact', 'fib']
while answer1 != 'stop':
    
    while True:
        operation = input("choose your operation ('add', 'sub', 'multiply', 'divide','checkeven', 'fact', 'fib')")
        if operation in answer2:
            break
        else:
            print("invalid input")
            pass
    if operation == 'checkeven':
        num1 = int(input("enter number to check whether its even or odd"))
        checkeven(num1)
    elif operation == 'fact':
        num1 = int(input("enter number to calculate its factorial"))
        result = fact(num1)
        print(result)
    elif operation == 'fib':
        num1 = int(input("enter number of terms to get fibonacci sequence"))
        fib(num1)
    else:
        num1 = int(input("enter The First Number: "))
        num2 = int(input("enter The Second Number: "))
        if operation == 'add':
            result= add(num1,num2)
            print(result)
        elif operation == 'sub':
            result= sub(num1,num2)
            print(result)
        elif operation == 'multiply':
            result= multiply(num1,num2)
            print(result)
        elif operation == 'divide':
            result= divide(num1,num2)
            print(result)
        else: 
            print("Unknwon erro")
        
        
    while answer1!="stop":
        answer1 = input("one more? (yes/stop): ")
        
        if answer1 != "yes" and answer1 !="stop" :
            print("invalid input")
            continue
        else:
            break


