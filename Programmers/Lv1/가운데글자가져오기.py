# 문제 설명
# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.
#
# 재한사항
# s는 길이가 1 이상, 100이하인 스트링입니다.
# 입출력 예
# s	return
# "qwer"	"we"
# "abcde"	"c"
def solution(s):
    i = len(s)
    if i%2 == 0 :
        answer = s[(i//2)-1:(i//2)+1]
    else :
        answer = s[len(s)//2]
    return answer

def string_middle(str):
    # 함수를 완성하세요

    return str[(len(str)-1)//2:len(str)//2+1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(string_middle("power"))