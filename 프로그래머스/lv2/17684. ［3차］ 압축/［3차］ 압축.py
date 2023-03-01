"""
LZW 압축 알고리즘
1. 길이 1 단어 모두 포함 -> 사전 초기화
2. 사전 내 입력값과 일치하는 가장 긴 문자열 w 탐색
3. w에 해당하는 사전의 Index 출력 & 입력에서 w 제거
4. 미처리 글자 c -> w+c에 해당하는 단어 등록
5. 2번으로 회귀
"""
import string
INDEX = list(string.ascii_uppercase) # index 1씩 작은것 주의

def solution(msg):
    global INDEX
    
    answer = []
    idx = 0
    while idx <= (len(msg)-1) :
        tmp = ''
        for k in range(len(msg), idx, -1) :
            msgIndex = search(msg[idx:k])
            if msgIndex == -1 :
                tmp = msg[idx:k]
                continue
            answer.append(msgIndex)
            addNewWord(tmp)
            idx = k
            break
    return answer

def search(s) :
    for i in range(len(INDEX)) :
        if INDEX[i] == s :
            return i+1
    return -1

def addNewWord(s):
    global INDEX
    INDEX.append(s)
    