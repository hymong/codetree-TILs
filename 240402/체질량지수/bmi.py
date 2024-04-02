input_value = input()
h, w = map(int, input_value.split())
b = w/(h/100)**2
print(int(b)) 
if b >= 25 :
    print("Obesity")

#소수점 출력
#print(f"{변수.?f}")