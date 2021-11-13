# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다.
# 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다.
# "z"는 1만큼 밀면 "a"가 됩니다.
# 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.
def solution(s, n):
    ls = []
    for a in s :
        if a.isspace() :
            ls.append(a)
        else :
            ascii = ord(a)
            if ascii >= 65 and ascii < 91:
                if (ascii+n) >= 91 :
                    ascii = (ascii+n) - 26
                    new_w = chr(ascii)
                else :
                    new_w = chr(ascii+n)
            elif ascii >= 97 and ascii < 123 :
                if (ascii+n) >= 123 :
                    ascii = (ascii+n) - 26
                    new_w = chr(ascii)
                else :
                    new_w = chr(ascii+n)
            ls.append(new_w)
    return ''.join(ls)

print(solution("a B z", 4))
print(ord("a"))

def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)

import string
def caesar(s, n):
    result = ""
    base = ""
    for c in s:
        if c in string.ascii_lowercase:
            base = string.ascii_lowercase
        elif c in string.ascii_uppercase:
            base = string.ascii_uppercase
        else:
            result += c
            continue
        a = base.index(c) + n
        result += base[a % len(base)]
    return result