def solution(n):
    answer = 0
    
    twobin = bin(n)
    cnt = sum(1 for n in str(twobin) if n == '1')
    
    while 1:
        n = n+1
        
        twobinWhile = bin(n)
        cntWhile = sum(1 for n in str(twobinWhile) if n == '1')
        
        if cnt == cntWhile:
            return n
