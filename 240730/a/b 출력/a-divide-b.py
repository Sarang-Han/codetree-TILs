a, b = map(int, input().split())

quotient = a // b
remainder = a % b
decimal = ""

for _ in range(20):
    remainder *= 10
    digit = remainder // b
    decimal += str(digit)
    remainder %= b

# 소수점 이하 자릿수 맞추기 (내림 처리)
decimal = decimal[:20]

print(f"{quotient}.{decimal}");