input_value = input()
input_value2 = input()

_A_math_score, _A_english_score = map(int, input_value.split())
_B_math_score, _B_english_score = map(int, input_value2.split())

if _A_math_score > _B_math_score and _A_english_score > _B_english_score:
    print("1")
else:
    print("0")