from itertools import combinations

def solution(number):
    
    items = combinations(number, 3)
    
    
    return sum(1 for item in items if sum(item) == 0) 