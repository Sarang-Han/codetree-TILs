is_mupt = True

for i in range(5):
    n = int(input())
    if n % 3 != 0:
        is_mupt = False

print(1 if is_mupt else 0)