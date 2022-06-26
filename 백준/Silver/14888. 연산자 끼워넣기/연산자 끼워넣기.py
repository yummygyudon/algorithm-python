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