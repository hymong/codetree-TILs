input_value = input()
arr = input_value.split()

h = float(arr[0])
w = float(arr[1])

b = int(w/((h/100)**2))
#문제에서 버림이라는 단어에 주의!

print(b)

if b>25 : 
   print("Obesity")