input_value = input()
a, b, c = map(int, input_value.split())

# a가 가장 작은 경우
if a <= b and a <= c:
    print(a)
# a가 가장작지 않은 경우 중 b가 가장 작은 경우 
elif b <= a and b <= c:
    print(b)
# a가 가장작지 않고 b도 가장 작지 않으므로 c가 가장 작은 경우
else:
    print(c)