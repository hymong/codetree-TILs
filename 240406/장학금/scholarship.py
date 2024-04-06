input_value = input()
score_middle, score_last = map(int, input_value.split())

if score_middle >= 90 and score_last >= 95:
    print("100000")
elif score_middle >= 90 and score_last >= 90:
    print("50000")
else:
    print("0")