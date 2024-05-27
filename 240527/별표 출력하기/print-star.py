n = int(input())

for i in range(1,n+1):
    for x in range(i):
        print("*", end=" ")
    print()

for y in range(n-1,0,-1):
    for z in range(y):
        print("*", end=" ")
    print()