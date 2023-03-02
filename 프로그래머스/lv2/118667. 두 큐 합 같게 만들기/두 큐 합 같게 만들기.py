"""
- [ 하나의 큐 : pop -> 다른 큐에 : insert ] 과정을 통해 각 큐의 원소 합이 같도록
- 최소 횟수
"""
from collections import deque
TOTAL = 0
HALF = 0
def solution(queue1, queue2):
    global TOTAL, HALF
    TOTAL = (sum(queue1) + sum(queue2)) 
    if TOTAL % 2 != 0 :
        return -1
    HALF = TOTAL//2
    return getCountToMakeBest(queue1, queue2)
    
#     caseA = deque(queue1+queue2)
#     caseB = deque(queue2+queue1)
#     count = 0
#     for _ in range(len(queue1)) :
#         print(caseA)
#         print(caseB)
#         print(count)
#         if (sum(list(caseA)[:length]) == sum(list(caseA)[length:])) or (sum(list(caseB)[:length]) == sum(list(caseB)[length:])) :
#             return count
#         caseA.rotate(-1)
#         caseB.rotate(-1)
#         count += 1
    

def getCountToMakeBest(q1, q2) :
    # temp = q1 + q2
    sumOfQueue1, sumOfQueue2 = sum(q1), sum(q2)
    q1, q2 = deque(q1), deque(q2)
    count = 0
    limit = len(q1) * 4
    """
    sum() 연산 -> 시간 초과
    - 1차 개선 : 비교값에 쓰이는 합은 변수로 사용해서 sum() 연산 줄이기
    """
    while True :
        if not q1 or not q2 :
            return -1
        if count > limit :
            return -1
        if sumOfQueue1 == HALF:
            break 
        if sumOfQueue1 < HALF :
            moveVal = q2.popleft()
            q1.append(moveVal)
            sumOfQueue1 += moveVal
            sumOfQueue2 -= moveVal
        else :
            moveVal = q1.popleft()
            q2.append(moveVal)
            sumOfQueue1 -= moveVal
            sumOfQueue2 += moveVal
        count+=1
    print(count)
    return count
    
    
    