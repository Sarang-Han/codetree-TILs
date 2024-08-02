n = int(input())
cnt = 1

while True:
    n /= cnt
    cnt += 1
    if n <= 1:
        break
print(cnt-1)