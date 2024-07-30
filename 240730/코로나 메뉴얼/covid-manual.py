case = 0
for i in range(3):
    symp, temp = input().split()
    temp = int(temp)

    if symp == "Y" and temp >= 37 :
        case += 1

print("E" if case >= 2 else "N")