S = list(input())
status = True
cnt = 0
start = S[0]
for s in S :
    if s == start and status :
        continue
    elif s != start and status:
        cnt += 1
        status = False
        continue
    elif s != start and status == False :
        continue
    elif s == start and status ==False :
        status = True
print(cnt)


