n = int(input())

for i in range(n):
    for y in range(n-i):
        print("*", end=" ")
    print()

for x in range(n-2,-1,-1):
    for z in range(n-x):
        print("*", end=" ")
    print()