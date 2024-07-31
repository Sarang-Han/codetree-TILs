n = int(input())
div = 0

for i in range(1, n):
    if n % i == 0:
        div += i

print("P" if div == n else "N")