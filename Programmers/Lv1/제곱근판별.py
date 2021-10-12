def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return int((sqrt + 1) ** 2)
    return -1

def solution(n):
    import math
    sqrt = math.sqrt(n)
    if (sqrt-int(sqrt)) != 0 :
        answer = -1
    else :
        answer = int((sqrt+1)**2)
    return answer

print(nextSqure(121))
print(nextSqure(3))
print(solution(121))
print(solution(3))
