def solution(n, lost, reserve):
    answer=0
    lost.sort()
    reserve.sort()
    
    able = [True]*(n+1)
    canGive = [False]*(n+1)
    able[0] = False
    for i in lost :
        able[i] = False
    
    arr = []
    
    for j in reserve :
        if j in lost :
            # 여벌 옷 있는 학생도 도난 당할 수 있음 -> 못빌려줌
            # 하지만 수업은 들을 수 있음
            able[j] = True
            arr.append(j)
            continue
        # 여벌옷이 있으면서 도난 당하지 않은 학생
        canGive[j] = True
    
    for k in lost :
        if (k in arr) or able[k] :
            continue
        if able[k-1] and canGive[k-1]:
            canGive[k-1] = False
            able[k] = True
        elif k < n :
            if able[k+1] and canGive[k+1] :
                able[k] = True
                canGive[k+1] = False
    for a in able[1:] :
        if a:
            answer+=1
    return answer