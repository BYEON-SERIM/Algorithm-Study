def solution(x, n):
    answer = []
    answer.append(x)
    
    for _ in range(n-1):
        answer.append(answer[-1]+x)

    return answer