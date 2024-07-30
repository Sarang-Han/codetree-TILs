gen = int(input())
old = int(input())

if gen == 1 :
    if old >= 19 :
        print("WOMAN")
    else :
        print("GIRL")
else :
    if old < 19 :
        print("BOY")
    else :
        print("MAN")