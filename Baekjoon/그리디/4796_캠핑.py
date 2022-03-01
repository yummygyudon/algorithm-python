n = 1
while True :
    P, L, V = map(int, input().split())
    if P == 0 and L == 0 and V ==0 :
        break
    able = V // L
    more = V%L
    # 16일일때 10일 but 계산 하면 able = 2, more = 0
    # 8일중 5일 가능한데 만약 휴가 남은 일자가 3일 남았는데 나머지가 4일 남을 경우
    # 5 8 22
    # able = 2 more = 6이 나오는데
    # 5일만 이용가능하지만 6이 나머지로 나오게되서 반례가 된다.
    if P < more :
        more = P
    print(f"Case {n}: {able*P + more}")
    n +=1
