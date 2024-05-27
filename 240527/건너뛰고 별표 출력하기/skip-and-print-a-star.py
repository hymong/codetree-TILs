n = int(input())

for i in range(n-1,-1,-1):
    for x in range(n-i):
        print('*', end="")
    print("\n")

for y in range(1,n):
    for z in range(n-y):
        print('*', end="")
    print("\n")