cnt = 0
sum = 0

while True:
    n = int(input())
    if n > 29 :
        break
    sum += n
    cnt += 1

print(f"{sum/cnt:.2f}")