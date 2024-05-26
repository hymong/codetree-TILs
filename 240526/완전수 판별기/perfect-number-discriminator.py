n = int(input())
n_list = []

for i in range(1,n):
    if n%i == 0:
        n_list.append(i)
    
sum_n = 0
for i in range(len(n_list)):
    sum_n += n_list[i]

if sum_n == n:
    print("P")
else:
    print("N")