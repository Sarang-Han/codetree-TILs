a, b = map(int, input().split())
is_exist = False

for i in range(a, b+1):
    if 1920 % i == 0 and 2880 % i == 0:
        is_exist = True

print(1 if is_exist == True else 0)