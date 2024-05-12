# a를 b로 나누어서 몫 만 살리는 과정을 21번 반복하면 된다!!

a, b = map(int, input().split())
c = a%b
print(a//b,end="")
print(".",end="")
for i in range(20):
    # c에 10을 곱해주어야 한다!!
    d = (c*10) // b
    # (c*10)%d 가 다음 나눗셈의 대상이 되어야 한다.
    c = (c*10)%b
    print(d, end="")