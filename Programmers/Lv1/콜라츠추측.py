def solution(num):
    i = 0
    if num == 1 :
        return 0
    while True:
        if i == 500 :
            answer = -1
            break
        if num == 1:
            answer = i
            break
        if num % 2 == 0 :
            num = num/2
        else :
            num = (num*3) + 1
        i += 1
    return answer