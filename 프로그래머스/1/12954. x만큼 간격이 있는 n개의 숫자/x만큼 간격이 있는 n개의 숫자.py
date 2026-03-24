def solution(x, n):
    answer = []
    
    answer.append(x)
    num = x
    
    while len(answer) <= n-1:
        num += x
        answer.append(num)
        
    
    return answer