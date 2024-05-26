n = int(input())
n_list = []

for i in range(1, n+1):
    if i%2 == 0 :
        continue
    if i%3 == 0 and i%9 != 0:
        continue
    a = str(i)
    if a[-1] == str(5):
        continue
    n_list.append(i)

for i in range(len(n_list)):
    print(n_list[i], end=" ")