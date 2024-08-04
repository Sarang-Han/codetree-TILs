n = int(input())
is_compos = False

for i in range(2, n):
    if n % i == 0:
        is_compos = True

print("C" if is_compos == True else "N")