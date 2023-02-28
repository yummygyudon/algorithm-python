import math
def solution(n, k):
    strNumber = makeNumber(n,k)
    tmp = ''
    primeCount = 0
    # endFlag = True
    # print(strNumber.split("0"))
    elements = strNumber.split('0')
    # print(elements)
    for elem in elements :
        if elem :
            if isPrime(int(elem)) : 
                primeCount += 1
                    
    # for s in strNumber :
    #     print(s)
        # if int(s) > 0 :
        #     endFlag = False
        #     tmp += s
        # elif int(s) == 0 and not endFlag:
        #     checkNum = int(tmp)
        #     print(checkNum)
        #     if isPrime(checkNum) :
        #         primeCount += 1
        #     tmp = ''
    # checkNum = int(tmp)
    # if isPrime(checkNum) :
        # primeCount += 1
    return primeCount

def makeNumber(num, k) :
    tmp = ''
    while True :
        if int(num // k) == 0 :
            tmp += str(num%k)
            break
        tmp += str(num % k)
        num = num // k
    return tmp[::-1]

def isPrime(n : int) :
    # check = [True] * (1000001)
    # check[1] = False
    # i = 2
    # while True :
    #     if i == n :
    #         break
    #     for k in range(2, int(math.sqrt(n))+1) :
    #         check[i*k] = False
    #     i += 1
    # print(check[:n+1])
    # for i in range(n+1) :
    #     if not check[i] :
    #         return False
    if n == 1 :
        return False
    for i in range(2, int(math.sqrt(n))+1) :
        if n % i == 0 :
            return False
    return True
        
    
        