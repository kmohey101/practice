a = input("enter you text to get check: ")

b = list(a)
b.reverse()
b= ''.join(b)
if a == b:
    print(" your text is palindrome")
else:
    print("The number isn't a palindrome!")