import math

def solution(n):
    if n <= 0:
        return -1
        
    mathSqrt = math.sqrt(n)
    
    if mathSqrt.is_integer():
        x = int(mathSqrt) 
        return (x + 1) ** 2
    else:
        return -1