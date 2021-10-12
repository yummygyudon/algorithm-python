def solution(n):
    str_n = list(str(n))
    sort_n = sorted(str_n, reverse=True)
    answer = int(''.join(sort_n))
    return answer

print(solution(47894435789))
print(solution(118372))