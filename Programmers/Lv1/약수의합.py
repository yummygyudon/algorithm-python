# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
#
# 제한 조건 :
# n은 0 이상 3000이하인 정수입니다.
#
# <입출력 예>
# n	| return
# 12	| 28
# 5	| 6

def solution(n):
    return sum([i if n%i == 0 else 0 for i in range(1,n+1)])

def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])