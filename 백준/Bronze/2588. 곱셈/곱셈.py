a = int(input())
b = list(input())
tsm=0
i = 0
for k in range(2,-1,-1):
    rs = a*int(b[k])
    print(rs)
    tsm += rs*(10**i)
    i+=1
print(tsm)