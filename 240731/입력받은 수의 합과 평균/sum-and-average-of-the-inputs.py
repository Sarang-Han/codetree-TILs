n = int(input())
sum = 0

for i in range(n):
    num = int(input())
    sum += num

print(f"{sum} {sum/n:.1f}")