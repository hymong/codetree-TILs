input_value = input()
a, b, c = map(int, input_value.split())

if a <= b and a <= c:
    print(a)
if b <= a and b <= c:
    print(b)
if c <= a and c <= b:
    print(c)