a, b = map(int, input().split())

quotient = a // b
remainder = a % b
decimal = ""

for _ in range(20):
    remainder *= 10
    digit = remainder // b
    decimal += str(digit)
    remainder %= b

# 반올림 처리
if remainder >= b // 2:
    decimal = str(int(decimal) + 1)

# 소수점 이하 자릿수 맞추기
decimal = decimal.ljust(20, '0')

print(f"{quotient}.{decimal}")