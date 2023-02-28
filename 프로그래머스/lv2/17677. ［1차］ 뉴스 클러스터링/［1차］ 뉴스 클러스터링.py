LIST_A, LIST_B = [],[]
COUNTER_A, COUNTER_B = dict(), dict()
MULTI = 65536
import re
import math
from collections import Counter
def solution(str1, str2):
    global LIST_A, LIST_B
    listA, listB = makeListOf(str1), makeListOf(str2)
    listA.sort()
    listB.sort()
    LIST_A, LIST_B = listA, listB
    makeCounter()
    
    if not LIST_A and not LIST_B :
        return MULTI
    else :
        # print("COUNTER_A : ",COUNTER_A)
        # print("COUNTER_B : ",COUNTER_B)
        u, i = 0, 0
        union = list(COUNTER_A.keys() | COUNTER_B.keys())
        inter = list(COUNTER_A.keys() & COUNTER_B.keys())
        # print("union", union)
        # print("inter", inter)
        for e in inter :
            i += min(COUNTER_A.get(e), COUNTER_B.get(e))
        for e in union :
            if e in inter :
                u += max(COUNTER_A.get(e), COUNTER_B.get(e))
            elif e in LIST_A :
                u += COUNTER_A.get(e)
            elif e in LIST_B :
                u += COUNTER_B.get(e)
        # print("i : ",i)
        # print("u : ",u)
        
        return math.floor((i/u)*MULTI)

def makeListOf(strVal) :
    result = []
    for i in range(len(strVal)-1) :
        target = strVal[i:i+2]
        if re.findall('[a-zA-Z]{2}', target) :
            result.append(target.upper())
    return result

def makeCounter() :
    global COUNTER_A, COUNTER_B
    COUNTER_A = dict(Counter(LIST_A))
    COUNTER_B = dict(Counter(LIST_B))
