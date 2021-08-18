import random
def game(comp,you):
    if comp == you:
        return None
    elif comp ==  'b':
        if you == 'bu':
            return False
        elif you == 'g':
            return True
    elif comp == 'bu':
        if you == 'g':
            return False
        elif you == 'b':
            return True
    elif comp == 'g':
        if you == 'b':
            return False
        elif you == 'bu':
            return True
print ("Computer turn : chose Bomb(b),Building(bu) and Gun(g)? ")
r = random.randint(1,3)
if r == 1:
    comp = "b"
elif r == 2:
    comp = 'bu'
elif r == 3:
    comp = "g"
you = input("Your turn : chose Bomb(b),Building(bu) and Gun(g)? ")
a = game(comp,you)
print (f"You chose {you}")
print (f"Computer chose {comp}")
if a == None:
    print ("The game is tie!")
elif a == False:
    print ("You lost this game")
elif a == True:
    print ("You win this game ")
