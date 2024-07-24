time = list(map(int, input().split(":")))
time[0] += 1
time[0] = str(time[0])
time[1] = str(time[1])
print(time[0]+":"+time[1])