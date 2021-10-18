import random
a=random.randint(1, 9)
d=-1
turn=0
while turn<5:
    turn+=1
    d=int(input("Choose a number between 1 and 9: "))
    if a>d:
        print("Choose a bigger number")
        continue
    if a<d:
        print("Choose a smaller number")
        continue
    if a==d:
        print("You chose Corect")
        break
else:
    print("You Lose!")
