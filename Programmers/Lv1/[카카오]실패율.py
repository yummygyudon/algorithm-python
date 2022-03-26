def solution(N, stages):
    result =[]
    players = len(stages)

    for i in range(1, N+1) :
        p = stages.count(i)

        if players > 0 :
            fail_rate = p / players
        else :
            fail_rate = 0
        result.append([1 - fail_rate, i])
        players -= p
    result.sort(key = lambda x : x[0])
    for i in range(len(result)) :
        result[i] = result[i][1]
    return result