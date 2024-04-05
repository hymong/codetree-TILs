input_value = input()
a, b, c = map(int, input_value.split())

if b > a and b < c:
    print("1")
else:
    print("0")