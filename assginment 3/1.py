def add_to_tuple(old,new_item):
    new_tuple = list(old)
    new_tuple.append(new_item)
    new_tuple = tuple(new_tuple)
    return new_tuple

t = ("apple","bannan")
item = input("enter ur item ")
print(add_to_tuple(t, item))
