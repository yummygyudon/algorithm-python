def solution(slice, n):
    if not n%slice :
        return (n//slice)
    
    return (n//slice) + 1