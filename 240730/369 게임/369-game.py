n = int(input())
i = 1

while i <= n :
    if i % 3 == 0 :
        print(0, end = " ")
    elif list(i) in [3, 6, 9]:
        print(0, end = " ")
    else :
        print(i, end = " ")
    i += 1