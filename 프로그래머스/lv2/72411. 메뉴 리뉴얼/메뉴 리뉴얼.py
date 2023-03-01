"""
코스 요리 만들기
    - 각 손님들 주문 : 가장 많이 함께 주문한 단품 메뉴들로 구성
    - 최소 2가지 이상의 단품메뉴
    - 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합만 후보에 포함
    
* course : 코스구성 단품 음식 종류 수 ( 2 : 2가지 단품 구성 코스를 원함 )
    - 서로 다른 코스가 동일한 주문횟수를 가지면 둘다 삽입
    - 적은 주문횟수는 모두 버림
    
"""
from itertools import combinations
from collections import Counter
COURSE =[]
# COURSE_MENU = dict()

def solution(orders, course):
    global COURSE_MENU, COURSE
    COURSE = course
    totalOrder = [list(o) for o in orders]
    for order in totalOrder :
        order.sort()
    
    passMenu = []
        
    for n in COURSE :
        nowCourseCounter = Counter()
        for order in totalOrder :
            orderCounter = Counter(makeCombi(order,n))
            nowCourseCounter += orderCounter
        result = sorted(dict(nowCourseCounter).items(), key = lambda x : x[1], reverse = True)
        tmp = -1e9
        for k, v in result :
            if v < 2 or v < tmp:
                break
            passMenu.append(k)
            tmp = v
    
    passMenu.sort()
    return [''.join(menu) for menu in passMenu]

def makeCombi(order:list, n : int) :    
    return combinations(list(order), n)
