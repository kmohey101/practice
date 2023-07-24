'''l=[0,1]
for j in range(2,i):
    print(j)
    x = l[j-1] + l[j-2]
    l.append(x)
print(l)'''



def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
n = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i))
