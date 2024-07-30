thir = 0
fifth = 0

for i in range(10):
    n = int(input())
    if n % 3 == 0 :
        thir += 1
    if n % 5 == 0 :
        fifth += 1

print(thir, fifth, end = " ")