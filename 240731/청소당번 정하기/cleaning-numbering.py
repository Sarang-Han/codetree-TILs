n = int(input())
cnt1 = cnt2 = cnt3 = 0

for i in range(n):
    if i % 12 == 0:
        cnt3 += 1
    else:
        if i % 3 == 0:
            cnt2 += 1
        elif i % 2 == 0:
            cnt1 += 1

print(cnt1,cnt2,cnt3-1, end =" ")