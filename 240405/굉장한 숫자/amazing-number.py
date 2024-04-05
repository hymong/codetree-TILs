# and는 or 보다 연산자 우선순위가 높다!
n = int(input())

if (n % 2 == 1 and n % 3 == 0) or (n % 2 == 0 and n % 5 ==0):
    print("true")
else:
    print("false")