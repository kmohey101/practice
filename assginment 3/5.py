l = ["apple","bannan"]
words=1
letter = 0
for i in l :
    for j in i:
        letter+=1
    print(f"{words} word has {letter} letters ")
    letter = 0
    words+=1