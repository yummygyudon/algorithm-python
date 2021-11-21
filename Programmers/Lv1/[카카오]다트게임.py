# import random
# print(random.choice(["*", "#"]))
# answer = 0
# s = "1S2D*3T"
# import re
# num = re.findall("\d+", s)
# alp = re.findall("[A-Z]", s)
# opt = re.findall("[#,*]", s)
# print(num)
# print(alp)
# print(opt)
# print(s.index(opt[0]))
# print(s.index(alp))

# str 타입의 숫자들은 +=로 합친 숫자처럼 붙이기 가능하다..
#문자들도 누적합이 된다는 점..

answer = [] # 더할 값 넣을 빈 리스트 (비어있을 때 옵션도 되기 때문에 그냥 0으로 하면안됨.
num = '' # 10이 올 수도 있기 때문에 문자열 누적식으로 해야함
# for s in "1S2D*3T" :
#     if s.isdigit() :
#         num += s
#     if i == "S" :
#         answer.append(int(num)**1)
#         num = '' # 문자열 한번 만났으니 다시 업생주기
#     elif i == "D":
#         answer.append(int(num)**2)
#     elif i == "T":
#         answer.append(int(num)**3)
#     elif i ==

num = ['1','2','3','4']
n = ''
for i in num :
    n += i
print(n)

digit = [2, 4, 8]
print(digit*3)

d = '4'
print(d.isdigit())

# 카카오톡 게임별의 하반기 신규 서비스로 다트 게임을 출시하기로 했다. 다트 게임은 다트판에 다트를 세 차례 던져 그 점수의 합계로 실력을 겨루는 게임으로, 모두가 간단히 즐길 수 있다.
# 갓 입사한 무지는 코딩 실력을 인정받아 게임의 핵심 부분인 점수 계산 로직을 맡게 되었다. 다트 게임의 점수 계산 로직은 아래와 같다.
#
# 다트 게임은 총 3번의 기회로 구성된다.
# 각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.
# 점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산된다.
# 옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 아차상(#) 당첨 시 해당 점수는 마이너스된다.
# 스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
# 스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
# 스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
# Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
# 스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
# 0~10의 정수와 문자 S, D, T, *, #로 구성된 문자열이 입력될 시 총점수를 반환하는 함수를 작성하라.
#
# 입력 형식
# "점수|보너스|[옵션]"으로 이루어진 문자열 3세트.
# 예) 1S2D*3T
#
# 점수는 0에서 10 사이의 정수이다.
# 보너스는 S, D, T 중 하나이다.
# 옵선은 *이나 # 중 하나이며, 없을 수도 있다.
# 출력 형식
# 3번의 기회에서 얻은 점수 합계에 해당하는 정수값을 출력한다.
# 예) 37
#
# 입출력 예제
# 예제	dartResult	answer	설명
# 1	1S2D*3T	37	11 * 2 + 22 * 2 + 33
# 2	1D2S#10S	9	12 + 21 * (-1) + 101
# 3	1D2S0T	3	12 + 21 + 03
# 4	1S*2T*3S	23	11 * 2 * 2 + 23 * 2 + 31
# 5	1D#2S*3S	5	12 * (-1) * 2 + 21 * 2 + 31
# 6	1T2D3D#	-4	13 + 22 + 32 * (-1)
# 7	1D2S3T*	59	12 + 21 * 2 + 33 * 2

def solution(dartResult):
    answer = []
    num = ''
    for i in dartResult :
        if i.isdigit() :
            num += i
        elif i in ['S', 'D', 'T'] :
            if i == 'S' :
                answer.append(int(num))
                num = ''
            elif i == 'D' :
                answer.append(int(num)**2)
                num = ''
            else :
                answer.append(int(num)**3)
                num = ''
        elif i in ["*", "#"] :
            if i == "*" :
                if len(answer) == 1 :
                    answer[-1] = answer[-1]*2
                else :
                    answer[-1] = answer[-1]*2
                    answer[-2] = answer[-2]*2
            else :
                answer[-1] = answer[-1]*-1
    return sum(answer)




import re


def solution(dartResult):
    # 정규표현식 & re.compile & 딕셔너리 자료 활용
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1} #가져온 패턴의 3번쩨 ()는 '' 아무값 없기때문에 1 -> 그값 그대로
    p = re.compile('(\d+)([SDT])([*#]?)')
    # 하나의 패턴으로 정규표현식 엮기(complie) , ()로 점수/영역/옵션 형식 분리
    # 정규표현식 ? 는 '있어도 그만 없어도 그만' & 둘 중 어느것 하나라도 있으면 가져옴
    dart = p.findall(dartResult) # 각 회차단위로 위 지정 패턴에 해당하는 것들을 가져옴
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0: # 2개 이상을 경우
            dart[i-1] *= 2 # 이전 인덱스값은 이미 정규표현식적용된 객체를 계산한 정수값이 있음 (아래 계산식 필요 X)
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]] #

    answer = sum(dart)
    return answer

def solution(dartResult):
    answer = []
    dartResult = dartResult.replace('10','k') #10을 한글자 k로 변환한 문자열로 재정의
    point = ['10' if i == 'k' else i for i in dartResult]
    # k 재변환으로 10이 하나의 요소로 변화
    # 각 요소 [점수, 영역, (옵션), 점수, ..]로 나눠서 리스트 만들기
    print(point)

    i = -1 # 옵션을 위한 인덱스 값
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1) # sdt를 순서대로 배치해야하는 이유
        elif j == '*':
            answer[i] = answer[i] * 2 # 최근 인덱스 값에 2배
            if i != 0 : #2개 이상일때 (1개만 있지 않을 경우) _ 1개만 있을 경우, 위 계산만 하고 넘어감
                answer[i - 1] = answer[i - 1] * 2 # 최근 인덱스 직전 값에도 2배
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
            # 인덱스값이라고 할 수 있음
            # 첫 값들어가면 첫 값의 인덱스가 0이 되고 숫자일때만 더해지므로 위 문자들과는 별개로 각 인덱스가 됨.
    return sum(answer)