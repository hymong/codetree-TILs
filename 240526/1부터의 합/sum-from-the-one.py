n = int(input())
n_sum = 0


for i in range(1, n+1):
    n_sum += i
    if n_sum >= n:
        print(i)
        break