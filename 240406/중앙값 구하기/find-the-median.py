input_value = input()
a, b, c = map(int, input_value.split())

#a가 가장 큰 경우
if a > b and a > c:
    if b > c:
        print(b)
    else:
        print(c)

#a가 가장 크지 않은 경우
else:
    #b가 가장 큰 경우
    if b > c:
        if a > c:
            print(a)
        else:
            print(c)
    #c가 가장 큰 경우
    else:
        if a > b:
            print(a)
        else:
            print(b)