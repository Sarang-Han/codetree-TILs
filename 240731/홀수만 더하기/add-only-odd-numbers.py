n = int(input())
sum = 0

for i in range(n):
    num = int(input())
    if i % 2 != 0 and i % 3 == 0 :
        sum += num
print(sum)