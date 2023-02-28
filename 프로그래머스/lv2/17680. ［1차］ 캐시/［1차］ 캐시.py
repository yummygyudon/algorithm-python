"""
cache hit : 1
cache miss : 5

가장 오랫동안 참조 안된 것 제거
"""
# from collections import deque
# import heapq
# CACHE = []
# CACHE_SIZE = 0
# CITIES = []


# TIME = dict()
# TIME['hit'] = 1
# TIME['miss'] = 5

# def init() :
#     global CACHE, CACHE_SIZE, CITIES, TIME
#     CACHE = []
#     CACHE_SIZE = 0
#     CITIES = []

#     TIME = dict()
#     TIME['hit'] = 1
#     TIME['miss'] = 5

# def solution(cacheSize, cities):
#     global CACHE
#     global CACHE_SIZE
#     CACHE_SIZE = cacheSize
#     global CITIES
#     CITIES = deque(cities)
#     global TIME

#     answer = 0
#     index = 0
#     if CACHE_SIZE == 0 :
#         answer += len(CITIES)*TIME['miss']
#     elif len(CITIES) == 0 :
#         answer = 0
#     else :
#         while CITIES :
#             # print(CACHE)
#             nowCity = CITIES.popleft()
#             nowCity = nowCity.upper()
#             # print("now : ", nowCity)
#             index += 1
#             if not isCityInCache(nowCity) :
#                 # print("Miss")
#                 answer += TIME.get('miss')
#                 if len(CACHE) < CACHE_SIZE :
#                     heapq.heappush(CACHE, [index, nowCity])
#                 else :
#                     heapq.heappop(CACHE)
#                     heapq.heappush(CACHE, [index, nowCity])
#                 # index += 1
#             elif isCityInCache(nowCity) :
#                 # print("Hit")
#                 answer += TIME.get('hit')
#                 # index += 1
#                 # 갱신
#                 switchIndexOf(nowCity, index)  
#             # print()
#     return answer

# def isCityInCache(city) :
#     for index, savedCity in CACHE :
#         if savedCity == city :
#             return True
#     return False

# def switchIndexOf(city, newIndex) :
#     global CACHE
#     searchIndex = 0
#     for i in range(len(CACHE)) :
#         if CACHE[i][1] == city :
#             searchIndex = i
            
#     # CACHE[searchIndex][0] = newIndex
#     CACHE.pop(searchIndex)
#     heapq.heappush(CACHE, [newIndex, city])


def solution(cacheSize, cities):
    answer = 0
    i = 0              # 초기 캐시 인덱스
    cache = []
    if cacheSize == 0:                # 캐시 사이즈가 0이면,
        return len(cities)*5
    for c in cities:              
        city = c.upper()              # city 이름 대문자 통일
        if city in cache:             # 캐시에 이미 있는 city의 경우
            cache.remove(city)        # 해당 city 캐시에서 위치 재조정
            cache.append(city)
            answer += 1
        else:                         # 캐시에 없는 city의 경우
            answer += 5 
            if i < cacheSize:         # 아직 캐시에 빈 공간이 있다면
                cache.append(city)
                i += 1
            else:                     # 캐시에 빈 공간이 없다면
                cache.pop(0)          # 캐시 내부 city 하나 교체
                cache.append(city)

    return answer