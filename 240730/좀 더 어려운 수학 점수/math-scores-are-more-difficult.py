a, b = map(int, input().split())
c, d = map(int, input().split())

if a > c :
    print("A")
elif a == c :
    if b > d :
        print("B")
    else :
        print("A")
else:
    print("B")