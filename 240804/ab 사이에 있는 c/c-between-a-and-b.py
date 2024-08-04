a, b, c = map(int, input().split())
is_exist = False

for i in range(a, b+1):
    if i % c == 0:
        is_exist = True

print("YES" if is_exist == True else "NO")