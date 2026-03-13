def solution(n):
    answer = []
    answer.append(n)
    
    x = n
    
    while x != 1:
        if x % 2 == 0:
            x = x // 2
            answer.append(x)
        else:
            x = 3*x+1
            answer.append(x)
    
    return answer