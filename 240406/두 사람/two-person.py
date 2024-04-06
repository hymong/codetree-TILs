input_value1 = input()
input_value2 = input()

human1_age, human1_sex = map(str, input_value1.split())
human2_age, human2_sex = map(str, input_value2.split())

if (int(human1_age) >= 19 and human1_sex == "M") or (int(human2_age) >= 19 and human2_sex == "M"):
    print("1")
else: 
    print("0")