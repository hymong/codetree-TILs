input_value=input()
arr=input_value.split()

a=int(arr[0])
b=int(arr[1])

a+=b
#이 상태에서 a=a+b, b=b
b+=a
#이 상태에서는 a=a+b, b=b+a+b

print(a,b)