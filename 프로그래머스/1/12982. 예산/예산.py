def solution(d, budget):
    answer = 0
    
    d.sort()
    
    for n in d:   
        budget -= n    
        answer += 1
        
        if budget <0:
            answer -= 1
            return answer
        
    return answer