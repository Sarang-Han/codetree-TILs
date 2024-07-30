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

    # 반올림을 위해 21번째 자리를 계산
    remainder *= 10
    next_digit = remainder // b

    if next_digit >= 5:
        decimal = str(int(decimal) + 1).zfill(20)

    print(f"{integer}.{decimal[:20]}")