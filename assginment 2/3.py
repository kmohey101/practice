"""
user input no

find the pair sum of this no

example 7

4+3 or 5+2

"""

l1=[0,5,2,4,8,3,7]
l2= []
no = int(input("enter ur number to get sum of pairs : "))

for i in range(len(l1)):
    for j in range(len(l1)):
        test = no - l1[i]
        if test == l1[j]:
            l2.append([l1[i], l1[j]])
        else:
            continue
print(l1)
print(l2)


       
                


