def possible(answer) :
    for x, y, stuff in answer : # 첫번째(가로), 두번째(세로), 세번째 요소(기둥/보)
        if stuff == 0 : # 기둥
            ''' 
            1. y==0의 경우 : 바닥 시작  
            2. [x-1, y, 1] or [x,y,1] 의 경우 : 설치될 위치  "왼쪽 보의 오른쪽 끝" or "오른쪽 보의 왼쪽 끝" _ 오른쪽 방향으로 설치되었기 때문에 판별 가능 
            3. [x, y-1, 0] 의 경우 : 밑쪽이 기둥이라면 가능
            '''
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer :
                continue
            return False
        elif stuff == 1 : # 보
            ''' 
            1. [x, y-1 , 0] 의 경우 <왼쪽에 있는 기둥에 설치하고 싶은 경우 >:
                설치할 위치 아래가 기둥의 시작 == 설치할 위치가 기둥의 윗부분 (보 설치 가능)   
                                                    ▶ 오른쪽 방향으로 설치되기 때문에 "왼쪽 끝"이 기둥의 끝인지 검사
            2. [x+1, y-1 , 0] 의 경우 <오른쪽에 있는 기둥에 설치하고 싶은 경우> : 
                오른쪽 밑 지점에 기둥이 설치 되어있다 == 오른쪽 끝은 기둥의 윗부분 (보 설치 가능)
                                                    ▶ 오른쪽 방향으로 설치되기 때문에 "오른쪽 끝"이 기둥의 끝인지 검사 
            3. ( [x-1, y, 1] and [x+1, y, 1] ) 의 경우 : "두 보를 이어주는 보 "
                                                    ▶ 왼쪽 끝 & 오른쪽 끝 쪽에 설치되어있는 서로 다른 보가 있으면 가능
            '''
            if [x, y-1, 0] in answer or [x+1, y-1 , 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer) :
                continue
            return False
    return True

''' n 은 사용 안함 '''
def solution(n, build_frame) :
    answer = []
    # 순서대로 하나씩 설치해보기
    for frame in build_frame :
        x, y, stuff, operate = frame
        if operate == 0 : # 삭제
            ''' 제거 해보기 '''
            answer.remove([x, y, stuff])
            if not possible(answer) : # 가능한지 검사
                answer.append([x, y, stuff]) # 불가능하면 다시 설치
        if operate == 1 : # 설치
            ''' 설치 해보기 '''
            answer.append([x, y, stuff])
            if not possible(answer):  # 가능한지 검사
                answer.remove([x, y, stuff])  # 불가능하면 다시 제거
    return sorted(answer) # 정렬 결과 반환




if __name__ == "__main__" :
    n = 5
    build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
    print(solution(n, build_frame))

    m = 5
    build_frame2 = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
    print(solution(m, build_frame2))