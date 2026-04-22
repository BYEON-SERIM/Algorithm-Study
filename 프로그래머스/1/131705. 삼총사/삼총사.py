from itertools import combinations

def solution(number):
    answer = 0
    
    group = list(combinations(number, 3))
    
    return sum(1 for sumZero in group if sum(sumZero) == 0)