import sys
input = sys.stdin.readline

ODD = ['1','3','5','7','9']
oddCount = []
def dfs(cnt, numArr : list) :
    for num in numArr :
        if num in ODD :
            cnt += 1
    if len(numArr) == 1 :
        oddCount.append(cnt)
        return
    if len(numArr) <= 3 :
        temp = str(sum(list(map(int,numArr))))
        dfs(cnt,list(temp))
    else :
        for i in range(1, len(numArr) - 1):
            for k in range(i + 1, len(numArr)) :
                first = ''.join(numArr[:i])
                second = ''.join(numArr[i:k])
                third = ''.join(numArr[k:])
                temp = int(first) + int(second) + int(third)
                dfs(cnt, list(str(temp)))


NUM = list(input().rstrip())
dfs(0,NUM)
print(min(oddCount), max(oddCount), sep=" ")