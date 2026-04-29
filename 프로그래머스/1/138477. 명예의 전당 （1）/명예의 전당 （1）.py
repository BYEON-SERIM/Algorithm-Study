def solution(k, score):
    answer = []
    crown = []
    
    for s in score:
        crown.append(s)
        
        if len(crown) > k:
            crown.remove(min(crown))
            
        answer.append(min(crown))
    
    return answer