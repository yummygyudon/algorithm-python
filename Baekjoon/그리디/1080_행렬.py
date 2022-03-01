h, w = map(int,input().split())
arr_A = []
arr_B = []
for _ in range(h) :
    arr_A.append(list(map(int,list(input()))))
for _ in range(h) :
    arr_B.append(list(map(int,list(input()))))

def change(x, y) : # 범위가 왼쪽 위 지점을 기점으로 3x3범위 모두 바꿔주는 함수
    for i in range(x, x+3) :
        for j in range(y, y+3) :
            arr_A[i][j] = 1-arr_A[i][j]
cnt = 0

## 어째 함수내에선 범위를 벗어나면 그냥 적용이 안되는 듯 싶네요
#1x1 행렬에 적용하면 알아서 적용이 안되서 바뀌지 않음
# if len(arr_A[0]) < 3 or len(arr_A) < 3 :
#     print(-1)
# else :
for move_d in range(h-3+1) :
    for move_r in range(w-3+1):
        if arr_A[move_d][move_r] != arr_B[move_d][move_r] :
            cnt+=1
            change(move_d, move_r)
for i in range(h) :
    for j in range(w):
        if arr_A[i][j] != arr_B[i][j] :
            cnt= -1
print(cnt)



