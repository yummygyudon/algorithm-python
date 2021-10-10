# 문제 설명
# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.
#
# 제한 사항
# 두 수는 1이상 1000000이하의 자연수입니다.

# def solution(n, m):
#     if n > m :
#         if n%m == 0 :
#             answer = [m, n]
#         else :
#             answer = [1, n*m]
#     elif m > n:
#         if m%n == 0 :
#             answer = [n, m]
#         else :
#             answer = [1, n*m]
#     else :
#         answer = [1, n]
#     return answer


## 유클리드 호제법 사용
def solution(n, m):
    x, y = n, m
    while y:
        x, y = y, x % y
        #y가 0이 될때까지 y를 x%y(두수의 나머지 값)로 돌리면서 나눠감
    return [x, (n * m) // x]   #두 수의 곱을 최대공약수 나눈 값의 정수부분 = 최대공배수(나머지가 0이기 때문에 /해도됨)


print(15//3)