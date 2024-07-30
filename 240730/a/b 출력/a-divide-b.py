a, b = map(int, input().split())

quotient = a // b
remainder = a % b
decimal = ""

for _ in range(20):
    remainder *= 10
    digit = remainder // b
    decimal += str(digit)
    remainder %= b

print(f"{quotient}.{decimal}");