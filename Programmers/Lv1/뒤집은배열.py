def solution(n):
    str_n = list(str(n))
    answer = list(map(int,list(reversed(str_n))))
    return answer

print(solution(12345))
print(reversed(['1','2','3','4']))
