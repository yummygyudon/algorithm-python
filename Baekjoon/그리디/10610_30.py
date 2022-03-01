# 메모리 초과
# import itertools
# N = input()
# nums = [n for n in N]
# permu = list(itertools.permutations(nums))
# result= []
# for p in permu :
#     result.append(int(''.join(p)))
# result.sort(reverse=True)
# value = -1
# for r in result :
#     if r%30 == 0 :
#         value = r
#         break
# print(value)

#  30은 3과 10의 배수
# 3의 배수 : 각 자리 합이 3의 배수
# 10의 배수 : 첫자리가 0이여야함.

# 30의 배수 : 각 자리 합이 3의 배수이면서 첫자리가 0이여야함.
nums = list(input())
nums.sort(reverse=True)
tmp = 0
for i in nums :
    tmp += int(i)
if tmp%3 != 0 or '0' not in nums :
    print(-1)
else :
    print("".join(nums))



