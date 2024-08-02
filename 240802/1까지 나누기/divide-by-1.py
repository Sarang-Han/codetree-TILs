n = int(input())
cnt = 0
i = 1
while True:
    n /= i
    if n < 1:
        cnt += 1
        break
    cnt += 1
    i += 1
print(cnt)