import sys
input= sys.stdin.readline
TC = int(input())

basic_case = [0, 1, 2, 4]

def sum_case(n):
    if n == 1 :
        return basic_case[1]
    elif n == 2 :
        return basic_case[2]
    elif n == 3 :
        return basic_case[3]
    return sum_case(n-3)+sum_case(n-2)+sum_case(n-1)
for _ in range(TC):
    N = int(input())
    print(sum_case(N))