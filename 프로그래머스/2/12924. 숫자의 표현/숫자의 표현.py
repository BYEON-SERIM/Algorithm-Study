def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        nSum = 0
        
        for j in range(i,n+1):
            nSum += j
                
            if nSum == n:
                answer += 1
            elif nSum > n:
                break

    return answer