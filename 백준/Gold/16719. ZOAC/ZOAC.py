import sys
input = sys.stdin.readline

WORD = input().rstrip()
SIZE = len(WORD)
INDEXES = []
def dfs(startIndex,endIndex) :
    global INDEXES
    if startIndex == endIndex :
        return
    sortedWord = sorted(WORD[startIndex:endIndex])

    index = WORD.find(sortedWord[0],startIndex)
    INDEXES.append(index)
    INDEXES.sort()
    
    char = ''
    for idx in INDEXES :
        char += WORD[idx]
    print(char)

    dfs(index+1,endIndex)
    dfs(startIndex, index)

dfs(0, SIZE)