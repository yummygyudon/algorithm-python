import re
def solution(s):
    rmCover = s[2:len(s)-2]
    elements = list(rmCover.split("},{"))
    elements = [list(s.split(",")) for s in elements]
    elements.sort(key = lambda x : len(x))
    
    answer = []
    for elem in elements :
        for e in elem :
            if e in answer :
                continue
            else :
                answer.append(e)
    return list(map(int,answer))