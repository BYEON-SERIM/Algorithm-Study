def solution(score):
    sums = [s[0] + s[1] for s in score]
    
    sorted_sums = sorted(sums, reverse=True)
    
    answer = [sorted_sums.index(s) + 1 for s in sums]
    
    return answer