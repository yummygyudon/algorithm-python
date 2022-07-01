from collections import deque

def solution(n, info):
    answer = []
    # [조준 점수, 과녁판에 꽂힌 화살 현황]
    # 0부터 시작 -> 10-i 가 점수 -> 10 ~ 0
    q = deque([( 0, [0,0,0,0,0,0,0,0,0,0,0] )])
    mxDiff = 0
    
    while q :
        target, t_board = q.popleft()
        # 다 쏜 경우
        if sum(t_board) == n :
            appeach, lion = 0,0
            for i in range(11):
                if not (info[i]==0 and t_board[i]==0) : # info(어피치) 와 t_board(라이언) 이 둘 다 쏜 점수일 경우
                    if info[i] >= t_board[i] :
                        appeach += (10-i)
                    else :
                        lion += (10-i)
            if appeach < lion :
                diff = lion - appeach
                if diff < mxDiff :
                    continue
                if diff > mxDiff :
                    mxDiff = diff
                    answer.clear() # 원래 있던 승리 과녁 초기화
                # mxDiff와 값이 같거나 더 큰 경우를 append
                answer.append(t_board) 
        # 다 쐈는데도 아직 못이긴 경우
        elif sum(t_board) > n :
            continue
        # 10점까지 다쐈는데 아직 화살을 다 못쏜경우
        # 극단적으로 target 때, 안쏘고 다 넘어간 경우 대비
        elif target == 10 :
            tmp = t_board.copy()
            tmp[target] = n - sum(t_board) # 0점에 남은 화살 몰빵
            q.append((1e9, tmp)) # 1e9는 아무값
        # 화살 쏘기
        else :
            # 안쏘고 넘어가기
            tmp1 = t_board.copy()
            tmp1[target] = 0
            q.append((target+1, tmp1))
            # 한발 더 쏘기
            tmp2 = t_board.copy()
            tmp2[target] = info[target]+1
            q.append((target+1, tmp2))    
    
    if not answer :
        return [-1]
    elif len(answer) == 1 :
        return answer[0]
    else :
        # answer에 있는 모든 승리 경우의 과녁 중
        # 맨 마지막에 있는 과녁의 경우가 target을 가장 마지막까지 연기 -> 늦게 반복 종료
        # 낮은 점수에 많이 쏜 과녁가 맨 마지막에 위치
        return answer[-1]