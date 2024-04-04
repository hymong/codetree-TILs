input_value = input()
a , b = map(int, input_value.split()) 
import random

#Python에서는 print 함수 사용시 기본적으로 한 줄이 띄어지게 됩니다. 출력 후 뒤에 
#엔터가 아닌 공백을 출력하고 싶다면 print(값, end=" ") 형태로 작성해야 합니다.

if a < b:
    print("1",end = " ")
else :
    print("0",end = " ")

if a == b:
    print("1")
else :
    print("0")