import sys
input = sys.stdin.readline

# DUCK = ['q','u','a','c','k']
NEXT_SOUND = dict()
NEXT_SOUND['q'] = 'u'
NEXT_SOUND['u'] = 'a'
NEXT_SOUND['a'] = 'c'
NEXT_SOUND['c'] = 'k'
NEXT_SOUND['k'] = 'q'

RECORD = list(input().rstrip())
CHECKED = [False] * len(RECORD)
SIZE = len(RECORD)

if len(RECORD) % 5 != 0:
    print(-1)
    exit()

COUNT = 0
for i in range(SIZE-1) :
    """
    아직 세보지 않은 울음소리의 시작일 경우 & q 뒤에 확인해볼 울음소리가 있는 경우
    - 어차피 울음 소리가 끝
    """
    if RECORD[i] == 'q' and not CHECKED[i] :
        count = 1
        CHECKED[i] = True
        next = NEXT_SOUND.get(RECORD[i])
        for k in range(i+1,SIZE) :
            if RECORD[k] == next and not CHECKED[k]:
                count += 1
                CHECKED[k] = True
                next = NEXT_SOUND.get(RECORD[k])
        """
        비저
        """
        if count % 5 == 0 :
            COUNT += 1
        else :
            COUNT = 0
            break

if COUNT > 0 :
    print(COUNT)
else :
    print(-1)