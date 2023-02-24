from sys import stdin

input = stdin.readline
N, S = map(int, input().split())
NUMS = list(map(int, input().split()))
if S == 0 :
    COUNT = -1
else :
    COUNT = 0
def bt(elemQuant, value) :
    global COUNT
    if elemQuant == N :
        if value == S :
            COUNT += 1
        return
    # 자기 자신 원소로만 이루어지는 수열들이 각자만의 값을 유지하려면
    # 별도 요소 추가 없이 N 깊이 까지 내려가기
    bt(elemQuant+1,value)
    # 깊이가 1씩 늘어날 때마다 각 원소들이 추가된 bt()를 호출하고
    # 해당 bt()로 들어간 후 아래 작업을 모든 요소의 경우에서 연산한다.
    bt(elemQuant+1,value+NUMS[elemQuant])

bt(0,0)
print(COUNT)