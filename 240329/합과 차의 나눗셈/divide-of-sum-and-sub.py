input_value = input()
arr = input_value.split()

a = int(arr[0])
b = int(arr[1])

plus = float(a+b)
minus = float(a-b)
result = float(plus/minus)

print(f"{result:.2f}")