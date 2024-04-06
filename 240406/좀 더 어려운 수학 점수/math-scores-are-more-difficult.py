input_value_A = input()
input_value_B = input()
score_math_A, score_english_A = map(int, input_value_A.split())
score_math_B, score_english_B = map(int, input_value_B.split())

if score_math_A > score_math_B:
    print("A")
elif score_math_A < score_math_B:
    print("B")
elif score_english_A > score_english_B:
    print("A")
else: 
    print("B")