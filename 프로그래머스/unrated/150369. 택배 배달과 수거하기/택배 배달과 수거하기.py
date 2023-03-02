def solution(cap, n, deliveries, pickups) :
    space = [[0,0] for _ in range(n+1)]
    startD, startP = cap, cap
    distance = 0
    count = 0
    for i in range(n-1, -1, -1):
        # if deliveries[i] > 0 or pickups[i] > 0:
        nowD, nowP = deliveries[i], pickups[i]
        space[i][0] = space[i+1][0] - nowD
        space[i][1] = space[i+1][1] - nowP
        # print("위치 : ",i+1)
        if space[i][0] < 0 or space[i][1] < 0 : 
            goBack = ((i+1)*2)
            # count += 1
            while True :
                # print("[space] = ",space)
                if space[i][0] >= 0 and space[i][1] >= 0 :
                    break
                # if space[i][0] < 0 :
                space[i][0] += cap
                # if space[i][1] < 0 :
                space[i][1] += cap
                # space[i][0] -= nowD
                # space[i][1] -= nowP
                count += 1
            distance += goBack * count
            count = 0
    #     else : 
    #         print("[space] = ",space)
    #     print()
    # print(distance)
    return distance

            
            
            