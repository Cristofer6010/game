print ("what you want, if you want upside down tringle type 2 other wise type 1")
y = int(input())
if y==1:
    print("Enter the length of the star pattren tringle")
    b = int(input())
    for i in range(b + 1):
        i = i * "*"
        print(i)
elif y==2:
    print("Enter the length of the star pattren tringle")
    a = int(input())
    while (0 != a):
        a = a - 1
        b = (a+1) * "*"
        print(b)
else:
    print ("Invalid syntax")
