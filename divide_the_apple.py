print ("Hello,\n\tFriend\n")
try:
    noStudent = int(input("Enter number of apples harry have : "))
    minNo = int(input("Minimum apples you wants to donate for harry students : "))
    maxNo = int(input("Maximum apples you wants to donate for harry students : "))

    a = noStudent
    b = minNo
    c = maxNo

    if int(b) == int(c):
        print("This condition in not handle here but")
    elif int(b) > int(c):
        print("Type minimum number is less than maximum number")

    for i in range(int(b), int(c) + 1):
        if int(a) % i == 0:
            print(f"{i} is a devisar of {a}")
        else:
            print(f"{i} is not a devisar of {a}")

except Exception as e:
    print(e)
