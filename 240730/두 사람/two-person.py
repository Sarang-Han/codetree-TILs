first, s1 = input().split()
second, s2 = input().split()
first = int(first)
second = int(second)

if (first >= 19 or second >= 19) and (s1 == "M" or s2 == "M"):
    print(1)
else:
    print(0)