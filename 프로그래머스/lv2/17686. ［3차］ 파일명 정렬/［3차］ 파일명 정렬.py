"""
파일명 포함 숫자 반영 정렬

1. HEAD 부분 사전 정렬 -> 대소문자 구분 X
2. NUMBER 숫자순 정렬 -> 앞 0 무시
3. 입력 순서
def solution(file_names):
    filt = re.compile(r'([a-zA-Z\-\n.]+)([0-9]{0,5})(.*)')
    files = []
    for file_name in file_names:
        files.extend(filt.findall(file_name))
    files.sort(key=lambda x: (x[0].lower(), int(x[1])))
    answer = [''.join(i) for i in files]
    return answer
"""
import re
"""
13번, 20번 틀린 이유 예측 : Head에 공백이 있을 경우
"""
def solution(files):
    bucket = []
    # \n : 공백, .* : 끝나는 기준 이후 모든 값
    # compiler = re.compile(r'([a-zA-Z\-\n.]+)([0-9]{0,5})(.*)')
    for i in range(len(files)) :
        fileName = files[i]
        number = getNumber(fileName)
        head = getHead(number,fileName)
        tail = getTail(head+number,fileName)
        bucket.append([head,number,tail,i])
        # bucket.extend(compiler.findall(fileName))
    bucket.sort(key = lambda x : (x[0].upper(), int(x[1])))
    print(bucket)
    
    return [e[0]+e[1]+e[2] for e in bucket]

def getHead(number,fileName) :
    # tmpList = fileName.split(number)
    tmp = ''
    for s in fileName :
        if re.findall('[0-9]', s) :
            break
        tmp += s
    # return tmpList[0]
    return tmp

def getNumber(fileName) :
    tmp = ''
    numberFind = False
    numberCount = 0
    # for s in fileName :
    #     if re.findall('[0-9]', s) :
    #         if numberCount < 5 :
    #             numberFind = True
    #             tmp += s
    #         else :
    #             break
    #     elif numberFind :
    #         break
    tmpList = re.findall('[0-9]{1,5}',fileName)
    # return tmp
    return tmpList[0]

def getTail(headAndNumber, fileName) :
    tmpList = fileName.split(headAndNumber)
    # for s in fileName[::-1] :
    #     if re.findall('[0-9]', s) :
    #         break
    #     tmp = s + tmp
    
    return tmpList[1]
    