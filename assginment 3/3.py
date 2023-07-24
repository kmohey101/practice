def mult_list_items(l):
    result =1
    for x in l:
        result *= x   
    return result
l = [3,3,3,3]
print(mult_list_items(l))