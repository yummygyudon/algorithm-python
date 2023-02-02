import sys
input = sys.stdin.readline
N = int(input())
"""
순서대로 담아가야하는 것이 규칙 -> sort금지
"""
BOX = list(map(int, input().split()))

DP = [0] * N
"""
맨 처음 박스 = 1 로처리
(안해주면 처음부터 박스가 없는 상태로 시작하는 것 -> 말이 안되는 상황)
"""
DP[0] = 1
"""
2번째 박스부터 쭉 브루트포스처럼 모든 순서의 박스를 시작으로 DP 시작
( 박스가 총 1개이면 range(1,1)로 for문을 안돌고 끝냄 )
"""
for i in range(1,N) : # 1,2,3,4,5,6,7,8
    MAX = 1
    for k in range(i) :
        """
        앞에 있는 박스들을 돌면서 더 작은 박스일 경우,
        해당 박스안에 담겨있는 최대 박스의 수를 가져와서 MAX값 갱신
         
        +1(자기자신)
        """
        if BOX[i] > BOX[k] :
            # DP[i] = DP[k]+1
            case = DP[k]+1
            MAX = max(MAX, case)
    DP[i] = MAX

    # DP[i] = MAX
print(max(DP))