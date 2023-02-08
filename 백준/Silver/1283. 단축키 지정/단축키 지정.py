import sys
import string
input = sys.stdin.readline


N = int(input())

SMART_KEY = set()
""" 모든 단어 탐색 """
for _ in range(N):
    WORDS = list(input().rstrip().split())

    """" 1번과 2번의 방법을 수행 """
    for i in range(len(WORDS)):
        """ 현재 단어의 첫 글자가 단축기로 지정되어 있지 않다면 """
        if WORDS[i][0].upper() not in SMART_KEY:
            SMART_KEY.add(WORDS[i][0].upper()) # 현재 단어의 첫 글자를 단축기로 지정
            WORDS[i] = "[" + WORDS[i][0] + "]" + WORDS[i][1:] # 현재 단어의 첫 글자를 "[]"를 감싼 후 출력.
            print(" ".join(WORDS))
            """
            첫 번째 글자에서 발견될 경우에도 break
            -> 첫번째 단어의 첫 글자가 있으면 다음 단어의 첫글자로 넘어감
            """
            break

    else:
        """
        반복문이 break를 통과 X -> 처음부터 모든 글자 순회
        """
        # 3번의 방법을 수행
        done = False
        for i in range(len(WORDS)):
             # 현재 단어의 알파벳을 단축기로 사용했는지 유무

            # 반복문을 통해 모든 단어의 알파벳을 확인
            for k in range(len(WORDS[i])):
                # 현대 단어의 알파벳이 단축기로 지정되어 있지 않다면
                if WORDS[i][k].upper() not in SMART_KEY:
                    SMART_KEY.add(WORDS[i][k].upper()) # 현재 단어의 첫 글자를 단축기로 지정
                    done = True
                    WORDS[i] = WORDS[i][:k] + "[" + WORDS[i][k] + "]" + WORDS[i][k + 1:] # 현재 단어의 첫 글자를 "[]"를 감싼 후 출력.
                    print(" ".join(WORDS))
                    break
            if done:
                break

        # 반복문이 break를 통과하지 않았다면
        # 어떠한 알파벳으로도 단축기를 지정할 수 없는 것
        if not done :
            print(*WORDS)