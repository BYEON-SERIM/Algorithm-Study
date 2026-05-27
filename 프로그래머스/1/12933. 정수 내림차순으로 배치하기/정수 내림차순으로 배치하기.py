def solution(n):
    
    nStr = [i for i in str(n)]
    
    nStr.sort(reverse=True)
    
    return int("".join(nStr))