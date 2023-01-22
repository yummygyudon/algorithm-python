def solution(t, p):
    answer = 0
    tLen = len(t)
    pLen = len(p)
    p = int(p)
    for i in range(0,tLen - pLen + 1) :
        temp = int(t[i:i+pLen])
        if(temp <= p):
            answer+=1
    return answer