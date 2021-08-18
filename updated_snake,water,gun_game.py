pqr = []
ijk = []
lmn = []
i = 0
while i<=10:
    i = i+1

    import random

    print (f'chance {i}')

    def game(comp, you):
        """ This function compare the values which is choose by computer and user"""
        if comp == you:
            return None
        elif comp == "s":
            if you == "w":
                return False
            elif you == "g":
                return True
        elif comp == "w":
            if you == 'g':
                return False
            elif you == 's':
                return True
        elif comp == 'g':
            if you == 's':
                return False
            elif you == 'w':
                return True
        else:
            print ("Invalid Syntax !")

    def fill(you):
        """This function complete the name before see the user"""
        if you == "s":
            return ("Snake")
        elif you == "w":
            return ("Water")
        elif you == "g":
            return ("Gun")
        else:
            print("Invalid Syntax !")

    def fall(comp):
        """This function complete the name before see the user"""
        if comp == "s":
            return ("Snake")
        elif comp == "w":
            return ("Water")
        elif comp == "g":
            return ("Gun")
        else:
            print("Invalid Syntax !")

    print("Comp Turn: Choose ('s' for Snake),('w' for Water) and ('g' for gun):")
    a = ['s', 'w', 'g']
    comp = random.choice(a)
    print("Your Turn: Choose ('s' for Snake),('w' for Water) and ('g' for gun):")
    you = input()

    fell = fall(comp)
    full = fill(you)

    print(f'Comp chose {fell}')
    print(f"You Chose {full}")

    b = game(comp, you)

    if b == False:
        print("\tYou lose this game ")
    elif b == True:
        print("\tYou win !!!!!!!! \n\t\tThis Game")
    elif b == None:
        print("\tThe game is Tie")
    else:
        print("Invalid Syntax !")
    if b == True:
        pqr.append(1)
        bcd = pqr.count(1)
        print (f"You win {(bcd)} times")
    if b == False:
        ijk.append(1)
        harry = ijk.count(1)
        print(f"Comp win {(harry)} times")
    if b == None:
        lmn.append(1)
        cristofer = lmn.count(1)
        print(f"Game tie {(cristofer)} times")
