def solution(strings, n):
    answer = []
    
    for s in strings:
        answer.append((s[n], s))
    
    
    answer.sort()
    
    return [x[1] for x in answer]