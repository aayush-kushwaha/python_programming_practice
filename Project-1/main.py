import random
def gameWin(comp,you):
    if comp == you:
        return None
    # Check all the possibilities when a computer chose s
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    # Check all the possibilites when a computer chose w
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    #Check all the posibilities when a computer chose g
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("Comp Turn: Snake(s) Water(w) Gun(g)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input('Your Turn: Snake(s) Water(w) Gun(g)?')
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")
if a == None:
    print("The game is Tie!")
elif a == True:
    print("You Win!")
else:
    print("You Lose!")
    
    

            