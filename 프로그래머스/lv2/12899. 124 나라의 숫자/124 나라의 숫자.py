nums = [1,2,4]
def solution(n):
    answer = ""
    while n > 3 : #3으로 나눠서 몫이 0이 될 때까지
        idx = n % 3 
        nxt = n//3
        if idx == 0 :
            idx = 3
            nxt = nxt - 1 # 3으로 나뉜다는 것은 다음 Loop엔 다음 순서의 번호를 사용해야함.
        answer = str(nums[idx-1]) + answer # 진법 변환과 동일한 방법으로 해당 idx의 문자 이어붙이기
        n = nxt # n 갱신
        
    # 남은 n 처리하기
    answer = str(nums[n-1]) + answer
    return answer