a = int(input())

for i in range(1, a + 1):
    quot = i // 8
    remain = i % 7

    if i % 2 == 0 and i % 4 != 0:
        continue
    elif quot % 2 == 0:
        continue
    elif remain < 4:
        continue
    print(i, end=" ")