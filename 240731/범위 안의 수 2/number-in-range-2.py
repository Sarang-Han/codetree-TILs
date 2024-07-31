sum = 0
cnt = 0

for i in range(10):
    num = int(input())

    if -1 < num < 201 :
        sum += num
        cnt += 1

print(f"{sum} {sum/cnt:.1f}")