def solution(n):
    str_n = list(str(n))
    answer = list(map(int,list(reversed(str_n))))
    return answer

print(solution(12345))