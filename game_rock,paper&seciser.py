import random

def game(comp,you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
    elif comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False
    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False
print ("computer turn : chose Rock(r),Paper(p) and scirros(s)? ")
r = random.randint(1,3)
if r == 1:
    comp = 'r'
elif r == 2:
    comp = 'p'
elif r == 3:
    comp = 's'
you = input("Your turn : chose Rock(r),Paper(p) and scirros(s)? ")
a = game(comp,you)
print (f"Computer choose {comp}")
print (f"You choose {you}")
if a == None:
    print ("The game is tie")
elif a == True:
    print ("You win this game")
else:
    print  ("You lost this game")
