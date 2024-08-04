n = int(input())
is_prime = False

for i in range(1, n+1):
    if n % i == 0:
        is_prime = True
        break

print("P" if is_prime else "C")