def solution(s):
    answer = []
    
    last_seen = {}
    
    for i, c in enumerate(s):
        if c not in last_seen:
            answer.append(-1)
        else:
            answer.append(i - last_seen[c])
            
        last_seen[c] = i
        
    return answer