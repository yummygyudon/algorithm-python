"""
1순위 = 서비스 가입자를 최대한 늘리는 것 -> "최대한" : 그리디?
2순위 = 판매액 최대한 늘리는 것

사거나 서비스에 가입
일정 비율 이상 할인하는 이모티콘 구매 -> 일정 가격 이상이 되면 구매를 모두 취소하고 서비스에 가입
"""
from itertools import product
RATE = [10,20,30,40]
RATE_CASES = []

LENGTH = 0

E_PRICE = []
C_INFO = []

def solution(users, emoticons):
    global RATE_CASES, E_PRICE, C_INFO, LENGTH
    LENGTH = len(emoticons)
    RATE_CASES = list(product(RATE,repeat=LENGTH))
    E_PRICE = emoticons
    C_INFO = users
    
    allCase = []
    for case in RATE_CASES :
        allCase.append(checkCase(case))
    # print(allCase)
    allCase.sort(key = lambda x : (-x[0], -x[1]))
    # (서비스 가입수, 매출)
    return allCase[0]

def calPrice(rate, price) :
    return (100 - rate) * price / 100
    # return int((1-(rate/100))* price) 

def checkCase(rateCase) :
    join, sale = 0, 0
    discounted = [[rateCase[i] ,calPrice(rateCase[i],E_PRICE[i])] for i in range(LENGTH)]
    # print("dicounted : ",discounted)
    for customer in C_INFO :
        wannaRate = customer[0]
        limit = customer[1]
        buy = []
        for d in discounted :
            if d[0] >= wannaRate :
                buy.append(d[1])
        if sum(buy) >= limit :
            join += 1
        else :
            sale += sum(buy)
    return [join, sale]
    

