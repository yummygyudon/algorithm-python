def solution(n):
    answer = []
    for i in range(1, n+1) :
        if not i%2 == 0 :
            answer.append(i)
    return answer