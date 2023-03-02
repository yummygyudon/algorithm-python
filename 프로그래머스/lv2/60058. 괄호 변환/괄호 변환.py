"""
괄호 갯수는 맞음
짝이 안맞음
"""
import re
def solution(p) :
    return dfs(p)

def dfs(p) :
    if len(p) == 0 :
        return ''
    
    u, v = divideSec(p)
    if checkIsCorrect(u) :
        return u + dfs(v)
    else :
        tmp = '('
        tmp += dfs(v)
        tmp += ")"
        """
        단순 역순이 아닌 순서는 동일하되 각자의 방향을 바꿔야하는것
        """
        # tmpOfU = list(u[1:len(u)-1])
        tmpOfU = ["(" if e == ")" else ")" for e in u[1:len(u)-1]]
        # tmp += ''.join(tmpOfU[::-1])
        tmp += ''.join(tmpOfU)
        # print("reverse : ", tmpOfU[::-1])
        return tmp
        

# u,v 영역 나누기
def divideSec(p) :
    openCount, closeCount = 0,0
    uSection = ''
    vSection = ''
    for i in range(len(p)) :
        if p[i] == "(" :
            openCount += 1
        elif p[i] == ")" :
            # closeCount += 1
            openCount -= 1
            
        # if openCount == closeCount :
        if openCount == 0 :
            uSection = p[:i+1]
            vSection = p[i+1:]
            break
    return (uSection, vSection)
            
def checkIsCorrect(u) :
    openCount = 0
    for i in range(len(u)) :
        if u[i] == "(" :
            openCount += 1
        else :
            openCount -= 1
        if openCount < 0:
            return False
    return True
        
        