#실패
# def solution(strings, n):
    alps = [alp[n] for alp in strings]
    answer, ls = [], []
    for alp, string in zip(alps, strings) :
        if len(answer) == 0 :
            answer.append(string)
            ls.append(alp)
        else :
            if alp < ls[0] :
                ls.insert(0,alp)
                answer.insert(0,string)
            elif alp

# 정확도가 떨어짐 _ 되는 테스트는 별로 없음
def solution(strings, n):
    words = [word[n:] for word in strings]
    s_words = sorted(zip(strings,words), key=lambda x: x[1])
    return [zipped[0] for zipped in s_words]

# 정확도가 떨어짐 _ 되는 테스트는 별로 없음
def solution(strings, n):
    mix = []
    for s in strings :
        mix.append([s[n:], s])
    mix = sorted(mix, key=lambda x: x[0])
    return [ls[1] for ls in mix]

def solution(strings, n):
    words = [[word[n:],word] for word in strings]
    words.sort(key=lambda x: x[0])
    answer = []
    for ls in words :
        answer.append(ls[1])
    return answer

##정확도가 안나오는 이유를 모르겠다...
##블로그 참고해서 더 작성해보자..
#
#
#정답
def solution(strings, n):
    mix = []
    for s in strings :
        mix.append(s[n]+s)
    mix.sort()  #와....다른 리스트에 선언하면 안되고 단독 명령해야함.. NonTyep 오류 발생
    answer = []
    for s in mix :
        answer.append(s[1:])
    return answer

