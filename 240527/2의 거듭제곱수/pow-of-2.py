n = int(input())
# n = 2의 거듭제곱수
cnt = 1
while True:
    if n == 2:
        break
    n = n%2
    cnt += 1

print(cnt)