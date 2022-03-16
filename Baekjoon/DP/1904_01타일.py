# ㅋㅋㅋㅋㅋㅋㅋㅋ망할 15746
N = int(input())
def tile_case(n) :
    tile_basic = [0,1,2]
    if n >=3 :
        for i in range(3, n+1):
            tile_basic.append((tile_basic[i-1]+tile_basic[i-2])%15746)
    print(tile_basic[n])

tile_case(N)


# 런타임에러 (100%까지는 감)
# N = int(input())
# tile_basic = [0]*(N+1)
# tile_basic[1] = 1
# tile_basic[2] = 2
# for i in range(3,N+1):
#     tile_basic[i] = tile_basic[i-1]+tile_basic[i-2]
# print(tile_basic[N])