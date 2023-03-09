def solution(n):
    absoluteNeed = n//7
    if n%7 > 0 :
        absoluteNeed += 1
    return absoluteNeed