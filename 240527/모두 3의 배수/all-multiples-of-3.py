result = False

for i in range(5):
    n = int(input())
    if n%3 == 0:
        result = True
    else:
        result = False
        break

if result == True:
    print(1)
else:
    print(0)