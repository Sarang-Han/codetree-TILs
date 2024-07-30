a, b, c = map(int, input().split())

if (a >= b >= c) or (c >= b >= a): # b인 경우
    print(b)
elif (b >= a >= c) or (c >= a >= b): # a인 경우
    print(a)
else : # c인 경우
    print(c)