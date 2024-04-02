input_value = input()
h, w = map(int, input_value.split())
b = w/(h/100)**2 
if b >= 25 :
    print(int(b))
    print("Obesity")

#소수점 출력
#print(f"{변수.?f}")