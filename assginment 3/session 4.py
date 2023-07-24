'''
def add_to_tuple(old,new_item):
    new_tuple = list(old)
    new_tuple.append(new_item)
    new_tuple = tuple(new_tuple)
    return new_tuple

t = ("apple","bannan")
item = input("enter ur item ")
print(add_t"o_tuple('"t, item)"')
'''

'''
def sum_list_items(l):
    result=0
    for x in l:
        result += x
    return result
l = [2,2,2,2]
print(sum_list_items(l))
'''

'''
def mult_list_items(l):
    result =1
    for x in l:
        result *= x   
    return result
l = [3,3,3,3]
print(mult_list_items(l))
'''

'''
l=[5, 2 , 4 ]
l.sort()
print(l[0])
'''
'''
l=[5, 2 , 4 ]
l.sort()
print(l[-1])
'''

'''
l = ["apple","bannan"]
words=1
letter = 0
for i in l :
    for j in i:
        letter+=1
    print(f"{words} word has {letter} letters ")
    letter = 0
    words+=1
    
'''

'''
l1 = ["apple","bannan"]
l2=[]
for x in l1:
    l2.append(x)
    
print(l1,l2)
'''

'''
item = input("enter item to delete from (apple,bannan,cherry) ")
s1={"apple","bannan","cherry"}        
s1.remove(item)
print(s1)   
''' 

'''  
s1={"apple","bannan","cherry"} 
s2={"apple","bannan"} 
print(s2.issubset(s1))
'''

'''
s1 = {2, 3, 5, 7}
s1.clear()
print(s1)
'''

'''
s1 = {4, 2, 5, 9}
s1= list(s1)
s1.sort()
print(f"the smallest number is : {s1[0]} and the smallest number is : {s1[-1]}")
s1 = set(s1)
'''













































