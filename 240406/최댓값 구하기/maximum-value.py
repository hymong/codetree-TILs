input_value = input()
a, b, c = map(int, input_value.split())

if a > b and a > c:
    print(a)
if b > a and b > c:
    print(b)
if c > a and c > b:
    print(c)
if a == b == c:
    print(a)
elif a == b:
    print(a)
elif b == c:
    print(b)
elif a == c:
    print(a)