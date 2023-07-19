# rock paper scissor GAME
import random
moves =  ["rock", "scissor" ,"paper"]
answer = input("hello, do you want to start (y):")
while answer != 'n':
    
    while True:
        usermove = input("Enter your move (rock - scissor - paper)")
        if usermove in moves:
            break
        else:
            print("invalid input")
            pass
    
    pyMoveId = random.randrange(0,3,1)
    pyMove = moves[pyMoveId]
    print(f"python chose: {pyMove}")
    if usermove == "rock" and pyMove == "paper":
        print("py win hardluck :)!")
    elif usermove == "rock" and pyMove == "scissor":
        print("you win GoodJob :)!")
    elif usermove == "paper" and pyMove == "rock" :
        print("you win GoodJob :)!")
    elif usermove == "paper" and pyMove == "scissor":
        print("py win hardluck :)!")
    elif usermove == "scissor" and pyMove == "paper" :
        print("you win GoodJob :)!")
    elif usermove == "scissor" and pyMove == "rock":
        print("py win hardluck :)!")
    else:
        print("draw!")
    
    while answer!="n":
        answer = input("one more? (y/n): ")
        if answer != "y" and answer !="n" :
            print("invalid input")
            continue
        else:
            break
    
    