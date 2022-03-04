from collections import deque
from itertools import permutations
N = int(input())
nums = list(map(int,input().split()))
op_list = ["+", "-","*", "/"]
op_num = list(map(int,input().split()))
mx = -1e9
mn = 1e9

op = []
for i in range(len(op_num)):
    for k in range(op_num[i]) :
        op.append(op_list[i]) # 횟수만큼 연산자 기호 입력
# 숫자를 permutations하는 것이 아니라
# 숫자위치는 가만히 두고 연산자의 위치에 대해 permutation했어야 했다.
op_mix = list(permutations(op, N-1)) # 숫자 갯수보다 하나 적으니까

for om in op_mix :
    print(om)
    result = nums[0]
    for i in range(1,N) : # nums의 index용
        if om[i-1] == "+" :
            result += nums[i]
        elif om[i-1] == "-":
            result -= nums[i]
        elif om[i-1] == "*" :
            result *= nums[i]
        elif om[i-1] == "/" :
            result = int(result / nums[i]) # //= 불가능
            # if c_op[0] >0 :
            #     result += m[n_cnt]
            #     c_op[0] -= 1
            # elif c_op[1] > 0:
            #     result -= m[n_cnt]
            #     c_op[1] -= 1
            # elif c_op[2] > 0 :
            #     result *= m[n_cnt]
            #     c_op[2] -= 1
            # elif c_op[3] >0 :
            #     result = result//m[n_cnt]
            #     c_op[3] -= 1
    mx = max(mx, result)
    mn = min(mn, result)
print(mx)
print(mn)

## DFS 활용
from itertools import permutations
N = int(input())
nums = list(map(int,input().split()))
op_num = list(map(int,input().split()))
mx = -1e9
mn = 1e9

def dfs(depth, result, add, sub, multi, div) :
    global mx, mn
    if depth == N :
        mx = max(result, mx)
        mn = min(result, mn)

    if add :
        dfs(depth+1, result + nums[depth], add-1, sub, multi, div)
    if sub:
        dfs(depth+1, result - nums[depth], add, sub-1, multi, div)
    if multi:
        dfs(depth+1, result * nums[depth], add, sub, multi-1, div)
    if div:
        dfs(depth+1, int(result / nums[depth]), add, sub, multi, div-1)

dfs(1, nums[0],op_num[0],op_num[1],op_num[2],op_num[3])
print(mx)
print(mn)
    # if add == op[0] :
        #     if sub == op[1] :
        #         if multi == op[2] :
        #             if div == op[3] :
        #                 break
        #             else :
        #                 result = result//m[n_cnt]
        #                 div += 1
        #         else :
        #             result = result*m[n_cnt]
        #             multi += 1
        #     else :
        #         result = result - m[n_cnt]
        #         sub += 1
        # else :
        #     result = result + m[n_cnt]
        #     add +=1
        # n_cnt+=1


