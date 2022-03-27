def key_rotate(arr) :
    n = len(arr)
    m = len(arr[0])
    result = [[0]*m for _ in range(n)] # key 돌린 값 저장할 백지 이차원배열 ( 정사각이기때문에 n,m 순서 바뀌어도 됨. )
    for i in range(n) :
        for k in range(m) :
            # 정사각 키이기때문에 n에서 빼든 m에서 빼든 상관 X
            result[k][n-i-1] = arr[i][k]
    return result

def check(new_lock) : # key&lock을 겹쳐본 모습이 들어온
    lock_length = len(new_lock) // 3 # 확대햇었던 범위 줄여서 check해야함 _
    # ex 3x3이였을 때 " 중앙에 lock이 있는 " 9x9가 들어옴 → length == 3
    for i in range(lock_length, lock_length*2) :
        # lock_length * 2 == 6 → < 3, 4, 5 > 를 검사 == 즉, 가운데 " lock "을 검사하는것
        for j in range(lock_length, lock_length*2) :
            if new_lock[i][j] != 1 : # [key와 lock을 맞춘 상태] 가 완전히 안맞는 경우
                return False
    return True

def solution(key, lock) :
    N, M = len(lock[0]), len(key[0]) # 꼭 [0] 안해도 정사각이라 "행 수"로 세도 상관없음
    new_lock = [[0] * (N*3) for _ in range(N*3)]
    # lock 기준
    for i in range(N):
        for j in range(N) :
            new_lock[i+N][j+N] = lock[i][j] # 3배한 lock 중앙에 기존 lock 입력
    for _ in range(4) :
        key = key_rotate(key)
        '''
        밑 x,y 는 비교를 "시작할 위치"의 기준이기 때문에 3배한 길이를 비교하려면 2배길이부분에서 시작해야함
        ▶ 0의 위치 시작 ~ 2배 길이 뒤 위치 시작
        '''
        for x in range(N*2) :
            for y in range(N*2) :
                '''
                밑 i, k는  위반복문에서 정해진 시작 위치부터 키를 대입하기 위함
                키의 좌표
                '''
                # 열쇠 대입
                for i in range(M):
                    for k in range(M):
                        new_lock[x+i][y+k] += key[i][k]
                if check(new_lock) :
                    #lock 부분이 모두 돌기와 홈이 딱 맞아떨어져 1을 가지고 있으면
                    return True # 끝

                # check한 결과가 False인 경우, 더했던거 다시 원상복귀
                for i in range(M) :
                    for k in range(M) :
                        new_lock[x+i][y+k] -= key[i][k]
    return False







'''
<<프로그래머스>>
정확성: 72.0
합계: 72.0 / 100.0
'''
if __name__ == "__main__" :
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

    print(solution(key, lock))
    # if solution(key, lock) :
    #     print("true")
    # else :
    #     print("false")