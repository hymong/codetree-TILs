score = int(input())

level= "0" if score == 100 else "1~9"

print("pass") if int(level) == 0 else print("failure")

# '=' 대신에 '=='을 사용해야함!!!!