var = 1
chance = 10
n = 18
print ('Welcome to this guess the number game')
print ("Type any number : ")
a = int(input())
if a == n:
    print(" Congratulation,You win this gam")
elif (a<n):
    print ("A number which is guess by you is less than the lucky number")
elif (a>n):
    print ("A number which is guess by you is more than the lucky number")
while (a != 18):
    print ("Type number again ")
    chance = chance - 1
    var = var + 1
    print (f"you have only {chance} chance")
    if chance==0:
        print('You lost this game')
        break
    a = int(input())
    if (a < n):
        print("A number which is guess by you is less than the lucky number")
    elif (a > n):
        print("A number which is guess by you is more the lucky number")

    elif a == n:
        print (" Congratulation,You win this game")
        print (f"You comlete this game in {var} chance")
