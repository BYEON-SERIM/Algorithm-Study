from itertools import combinations

def solution(numbers):
    answer = []
    
    comb = list(combinations(numbers,2))
        
        
    return sorted(set([sum(s) for s in comb]))