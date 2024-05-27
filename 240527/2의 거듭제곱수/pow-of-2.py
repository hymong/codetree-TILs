n = int(input())
cnt = 1


while True:
    if n == 2:
        break
    else:
        n = n//2
        cnt += 1

print(cnt)