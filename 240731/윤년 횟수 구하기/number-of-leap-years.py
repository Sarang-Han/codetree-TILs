n = int(input())
cnt = 0

for i in range(1, n):
    if i % 4 == 0 :
        if i % 100 == 0 and i % 400 != 0 :
            pass
        cnt += 1
    else:
        pass

print(cnt)