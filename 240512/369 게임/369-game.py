n = int(input())


for i in range(1,n+1):
    if i < 10:
        if i%3 == 0:
            print(0)
        else:
            print(i,end=" ")
    elif i < 100:
        if i%3 == 0:
            print(0)
        else:
            a = i%3
            if a == 3:
                print(a)
            elif a == 6:
                print(a)
            elif a == 9:
                print(a)
            else:
                print(i, end=" ")