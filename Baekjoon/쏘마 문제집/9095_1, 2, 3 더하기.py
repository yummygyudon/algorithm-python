N = int(input())

def fibo(num) :
    if num == 1 :
        return 1
    elif num == 2 :
        return 2
    elif num == 3 :
        return 4
    else :
        return fibo(num-3) + fibo(num-2) + fibo(num-1)

for i in range(N):
    print(fibo(int(input())))
