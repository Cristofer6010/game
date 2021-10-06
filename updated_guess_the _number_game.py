try:
    print("\n\t\t\t\t\t!!!!! Welcome again to Guess the number game !!!!!\n")


    class Game:
        import random
        user1 = input("Enter first player name : ")
        user2 = input("\nEnter second player name : ")

        print(f"\t\t\t\nIt's {user1} chance to generate the difficulty for your friend {user2}\n")
        times0 = int(input("\nEnter how many times you want to play this game : "))

        print("Enter two number where you want to hide the lucky number ")
        value3 = int(input("Enter first number : "))
        value4 = int(input("Enter second number : "))
        value0 = random.randint(value3, value4)

        for j in range(1, times0 + 1):
            print("\tNOTE : Include first and last number also\n")
            xx = (times0 + 1) - j
            print(f"Your {j} chance\nChance left {xx} ")
            chose1 = int(input(f"Enter the lucky number between {value3} and {value4} : "))

            if chose1 == value0:
                print(f"\n\t!!!!!! You win this game !!!!!!\nYour lucky number is {value0}")
                break
            elif j == times0:
                print(f":( You lose ):\nYour lucky number is {value0}")
            elif chose1 > value0:
                print("Your lucky number is less than this number")
            elif chose1 < value0:
                print("Your lucky number is greater than this number")
            else:
                break


    class Game1(Game):
        import random

        user1 = Game.user1
        user2 = Game.user2
        print(f"\t\t\t\nIt's {user2} chance to generate the difficulty for your friend {user1}\n")
        times0 = int(input("\nEnter how many times you want to play this game : "))

        print("Enter two number where you want to hide the lucky number ")
        value3 = int(input("Enter first number : "))
        value4 = int(input("Enter second number : "))
        value0 = random.randint(value3, value4)

        for j in range(1, times0 + 1):
            print("\tNOTE : Include first and last number also\n")
            xx = (times0 + 1) - j
            print(f"Your {j} chance\nChance left {xx} ")
            chose1 = int(input(f"Enter the lucky number between {value3} and {value4} : "))

            if chose1 == value0:
                print(f"\n\t\t!!!!!! You win this game !!!!!\nYour lucky number is {value0}")
                break
            elif j == times0:
                print(f":(You lose ): \nYour lucky number is {value0}")
            elif chose1 > value0:
                print("Your lucky number is less than this number")
            elif chose1 < value0:
                print("Your lucky number is greater than this number")
            else:
                break


except Exception as e:
    print(e)
