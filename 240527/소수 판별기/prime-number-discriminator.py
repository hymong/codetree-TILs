n = int(input())
result = True

for i in range(2,n):
    if n%i == 0:
        result = False
        break

if result == True:
    print("P")
else:
    print("C")