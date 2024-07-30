a, b = map(int, input().split())

integer_part = a // b
decimal_part = ""
remainder = a % b

for _ in range(21):
    remainder *= 10
    digit = remainder // b
    decimal_part += str(digit)
    remainder %= b

# 반올림 처리
if remainder >= b // 2:
    decimal_part = str(int(decimal_part) + 1)

# 소수점 이하 자릿수 맞추기
if len(decimal_part) < 20:
    decimal_part += '0' * (20 - len(decimal_part))

print(f"{integer_part}.{decimal_part}")