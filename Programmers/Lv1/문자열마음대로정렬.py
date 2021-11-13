#실패
# def solution(strings, n):
#     alps = [alp[n] for alp in strings]
#     answer, ls = [], []
#     for alp, string in zip(alps, strings) :
#         if len(answer) == 0 :
#             answer.append(string)
#             ls.append(alp)
#         else :
#             if alp < ls[0] :
#                 ls.insert(0,alp)
#                 answer.insert(0,string)
#             elif alp

# 정확도가 떨어짐 _ 되는 테스트는 별로 없음
def solution(strings, n):
    words = [word[n:] for word in strings]
    s_words = sorted(zip(strings,words), key=lambda x: x[1])
    return [zipped[0] for zipped in s_words]

# 정확도가 떨어짐 _ 되는 테스트는 별로 없음
def solution(strings, n):
    mix = []
    for s in strings :
        mix.append([s[n:], s])
    mix = sorted(mix, key=lambda x: x[0])
    return [ls[1] for ls in mix]