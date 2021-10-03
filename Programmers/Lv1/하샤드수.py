#양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다.
#자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

# 제한 조건 :
# x는 1 이상, 10000 이하인 정수입니다.


def solution(x):
    result = x%sum([int(num) for num in str(x)])
    if (result == 0) :
        answer = True
    else :
        answer = False
    return answer


# 새로 알게된 것 (다른 풀이)
#return n % sum([int(c) for c in str(n)]) == 0
#True일 때만 알아서 return이 작동하기 때문에 return에 식을 넣어도 됨.
#0이 될때만 True이기 때문에 하샤드수일때만 return

# return True if n%a == 0 else False
# return에 if-else문 가능