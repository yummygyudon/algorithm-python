# def solution(n):
#     answer = []
#     for num in range(2,n+1) :
#         ls = [i for i in range(2,num+1) if num%i == 0]
#         if len(ls) == 1 :
#             answer.append(num)
#     return len(answer)
#
#
# def solution(n):
#     a=0
#     for num in range(2,n+1) :
#         ls = [i for i in range(2,num+1) if num%i == 0]
#         if len(ls) == 1 :
#             a+=1
#     return a

def solution(n):
    ls = [2,3,5,7]
    if n < 10 :
        for one in range(len(ls)) :
            if n <= ls[one] :
                return len(ls[:one])+1
    else :
        a = 4
        for num in range(10, n + 1):
            b = 0
            for s in ls:
                if num % s == 0:
                    b = 1
            if b == 0:
                a += 1
        return a

def solution(n):
    result = 0
    for i in range(1,n+1) :
        num = 0
        for j in range(1,i+1) :
            if i%j==0 :
                num += 1
        if num == 2 :
            result += 1
    return result


print(solution(10))