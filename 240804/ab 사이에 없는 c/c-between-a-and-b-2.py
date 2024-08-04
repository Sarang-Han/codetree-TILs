a, b, c = map(int, input().split())
has_No = False

for i in range(a, b+1):
    if i % c == 0:
        has_No = True
        break

print("NO" if has_No else "YES")