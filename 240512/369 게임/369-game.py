n = int(input())


for i in range(1,n+1):
    if i < 10:
        if i%3 == 0:
            print(0, end=" ")
        else:
            print(i,end=" ")
    elif i < 100:
        if i%3 == 0:
            print(0, end=" ")
        else:
            a = i%3
            if a == 3:
                print(a, end=" ")
            elif a == 6:
                print(a, end=" ")
            elif a == 9:
                print(a, end=" ")
            else:
                print(i, end=" ")