input_value1 = input()
input_value2 = input()
input_value3 = input()

sympton1, tempt1 = map(str, input_value1.split())
sympton2, tempt2 = map(str, input_value2.split())
sympton3, tempt3 = map(str, input_value3.split())

if sympton1 == "Y" and sympton2 == "Y" and sympton3 == "Y":
    if int(tempt1) >= 37 and int(tempt2) >= 37 and int(tempt3) >= 37:
        print("E")
    elif int(tempt1) >= 37 and int(tempt2) >= 37:
        print("E")
    elif int(tempt1) >= 37 and int(tempt3) >= 37:
        print("E")
    elif int(tempt2) >= 37 and int(tempt3) >= 37:
        print("E")
    else:
        print("N")
elif sympton1 == "N" and sympton2 == "Y" and sympton3 == "Y":
    if int(tempt2) >= 37 and int(tempt3) >= 37:
        print("E")
    else:
        print("N")
elif sympton2 == "N" and sympton1 == "Y" and sympton3 == "Y":
    if int(tempt1) >= 37 and int(tempt3) >= 37:
        print("E")
    else:
        print("N")
elif sympton3 == "N" and sympton1 == "Y" and sympton2 == "Y":
    if int(tempt1) >= 37 and int(tempt2) >= 37:
        print("E")
    else:
        print("N")
else:
    print("N")

    #이 문제는 arr써서 그냥 각자 type 지정 후 푸는 게 더 편했을지도!