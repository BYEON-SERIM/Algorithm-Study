import math

def solution(num_list):
    s_um = sum(num_list) ** 2
    p_rod = math.prod(num_list)
    
    return 1 if p_rod < s_um else 0