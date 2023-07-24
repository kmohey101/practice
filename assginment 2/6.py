l=[]
l2= []

def even_no_list(l):
    for i in range(len(l)):
        if l[i] % 2 == 0:
            L2 = l2.append(l[i])
    return l2
            
no_items = int(input("how many numbers will u enter? "))
lItems = []
for i in range(no_items):
    items = int(input("enter number :  "))
    lItems.append(items)

print(f"ur entered items are {lItems}")
l2 = even_no_list(lItems)
print(f"even numbers are {l2}.")

