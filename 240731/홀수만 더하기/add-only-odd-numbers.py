n = int(input())
sum = 0

for i in range(n):
    if i % 2 == 1 and i % 3 == 0 :
        sum += i
print(sum)