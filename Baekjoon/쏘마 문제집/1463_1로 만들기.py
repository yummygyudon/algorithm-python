X = int(input())
d= [0]*(X+1)

for i in range(2, X+1) : # 2인 이유는 1이 최종 목적값이기 때문에
    d[i] = d[i-1] +1
    # print(f"처음 직전 값의 d[i] 값을 가져온 d[{i}] : {d[i]}")
    if i % 2 == 0 :
        d[i] = min(d[i], d[i//2]+1)
        # print(f"2로 나눠지는 경우 d[i] : i는 {i} d[{i}]는 {d[i]}")
    if i % 3 == 0 :
        d[i] = min(d[i], d[i//3]+1)
        # print(f"3으로 나눠지는 경우 d[i] : i는 {i} d[{i}]는 {d[i]}")
    # print()
print(d[X])