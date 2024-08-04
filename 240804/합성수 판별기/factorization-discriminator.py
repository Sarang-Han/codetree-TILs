n = int(input())
is_compos = False

for i in (2, n+1):
    if n // i == 0:
        is_compos = True

print("C" if is_compos == True else "N")