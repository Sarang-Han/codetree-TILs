n = int(input())
i = 1

while i <= n:
    # 숫자를 문자열로 변환하여 각 자리를 확인
    digits = str(i)
    
    # 각 자릿수에 3, 6, 9가 포함되어 있으면 0을 출력
    if any(d in '369' for d in digits):
        print(0, end=" ")
    # 3의 배수인 경우 0을 출력
    elif i % 3 == 0:
        print(0, end=" ")
    # 그 외에는 숫자 자체를 출력
    else:
        print(i, end=" ")
    
    i += 1