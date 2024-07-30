a, b = map(int, input().split())

if a % b == 0:
    print(f"{a // b}.00000000000000000000")
else:
    integer = a // b
    remainder = a % b
    decimal = ""

    for _ in range(20):
        remainder *= 10
        digit = remainder // b
        decimal += str(digit)
        remainder = remainder % b

    remainder *= 10
    next_digit = remainder // b

    if next_digit >= 5:
        # 소수 부분을 정수로 변환하여 반올림하고, 다시 문자열로 변환
        decimal = str(int(decimal) + 1)

    print(f"{integer}.{decimal}")