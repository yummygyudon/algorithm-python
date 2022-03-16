# 시간 초과
#
# def pin_case(n) :
#     if n == 1 or n == 2:
#         return pin_basic[n]
#     return pin_case(n-2) + pin_case(n-1)
# N = int(input())
# print(pin_case(N))



pin_basic = [0, 1, 1]

def pin_case(n) :
    if n >= 3 :
        for i in range(3, N+1) :
            pin_basic.append(pin_basic[i-2] + pin_basic[i-1])

N = int(input())
pin_case(N)
print(pin_basic[N])