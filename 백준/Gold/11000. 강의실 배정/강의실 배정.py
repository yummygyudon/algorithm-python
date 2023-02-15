import sys
input = sys.stdin.readline

"""
최소 강의실 수 사용 경우의 수를 구하는게 아니라
모든 수업을 할 수 있는 최소한의 강의실 사용량을 구하는 것(겹쳐도 됨 : 1번째 끝나는 시간 <= 2번째 시작하는 시간 같은 강의장 사용)
"""

N = int(input())

LESSON = []
for _ in range(N) :
    # LESSON.append([start,end,abs(start-end)])
    LESSON.append(list(map(int, input().split())))

# LESSON.sort(key=lambda x : x[0])
LESSON.sort()

# nowLessonEnd = 0

"""
시도 1 : 시간 초과
"""
import heapq
onTime = []
heapq.heappush(onTime, LESSON[0][1])
count = 1
for start, end in LESSON[1:] :
    if onTime[0] <= start :
        heapq.heappop(onTime)
        count -= 1
    heapq.heappush(onTime, end)
    count+=1
# print(onTime)
print(count)