from collections import Counter
def solution(array):
    counter = dict()
    for x in array :
        if x in counter :
            counter[x] = counter.get(x) + 1
        else :
            counter[x] = 1
            
    counts = counter.values()
    MAX = max(counts)
    result = []
    
    for k,v in counter.items() :
        if v == MAX :
            result.append(k)
            
    if len(result) > 1 :
        return -1
    return result[0]