a, b, c = map(int, input().split())
min = min(a, b, c)

if a == min :
    print(1, end = " ")
else :
    print(0, end = " ")

if a == b == c :
    print(1)
else :
    print(0)