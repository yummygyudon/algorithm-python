''' 우선순위 큐 _ heapq 사용'''
import heapq
def solution(food_times : list, k : int) :
    if sum(food_times) <= k :
        return -1

    q = []
    idx = 1
    for f in food_times :
        heapq.heappush(q, [f, idx])
        idx += 1

    length = len(food_times)
    tmp = 0 # 먹는데 소요한 시간
    prev = 0 # 직전에 다 먹은 음식 시간
    ''' 지금까지 소요한 시간 + (이번에 먹을 음식 총 필요시간 - 이전 음식(다먹고 없는 음식)이 소요했던 시간 )'''
    while tmp + ( (q[0][0] - prev) * length ) <= k :
        now = heapq.heappop(q)[0] # 잔여 음식(잔여시간) 제일 짧게 남은 음식의 잔여시간
        tmp += ( now - prev ) * length
        # " * length "의 이유 : 이번 음식을 먹기위해 매 바퀴를 돌아야하는데
        #                       이 바퀴를 한 번 돌고 다시 이번 음식으로 넘어오려면
        #                       모든 음식들을 매번 한번씩 지나야 하기때문에
        length -= 1 # 음식 하나 클리어
        prev = now # 다음 음식의 총 필요시간에 빼줄 " 지금까지 걸린 시간 "

    result = sorted(q, key = lambda x: x[1]) # 음식 번호 기준 정렬
    return result[(k-tmp)%length][1]
    # (주어진 시간 - 최대한 먹을만큼 먹으면서 소요한 시간) % (남은 음식 수)

''' 효율성 0 점, 정확성 26/32 만 맞음'''
if __name__ == "__main__":
    food_times = [3, 1, 2]
    k = 5

    print(solution(food_times, k))