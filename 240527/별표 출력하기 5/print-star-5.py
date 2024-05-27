n = int(input())

for i in range(n,0,-1):
    for x in range(i):
        print("*"*i,end=" ")
    print()