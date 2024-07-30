case = 0
for i in range(3):
    symp, temp = input().split()
    temp = int(temp)

    if symp == "Y" and temp >= 37 :
        case += 1

if case >= 2 :
    print("E")
else :
    print("N")