import sys
input = sys.stdin.readline
N = int(input())
Map = []
for _ in range(N) :
    Map.append(list(map(int, input().rstrip())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x,y) :
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if Map[x][y] == 1 :
        global house_cnt
        Map[x][y] = 0
        house_cnt += 1
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False

cnt = 0
Each = []
house_cnt = 0
for i in range(N):
    for k in range(N) :
        if dfs(i,k) :
            Each.append(house_cnt)
            cnt+=1
            house_cnt = 0
print(cnt)
Each.sort()
for i in Each :
    print(i)