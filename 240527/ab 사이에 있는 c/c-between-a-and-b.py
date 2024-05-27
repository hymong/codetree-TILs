a, b, c = map(int, input().split())

multiple_c = "False"

for i in range(a, b+1):
    if i%c == 0:
        multiple_c = "True"
        break

if multiple_c == "True":
    print("YES")
else:
    print("NO")