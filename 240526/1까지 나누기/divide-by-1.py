n = int(input())
cnt = 1

for i in range(1,n+1):
    n //= i
    if n > 1:
        cnt += 1
    else:
        break

print(cnt)