import math

def solution(n, m):
    answer = []
    
    gcd = math.gcd(n,m)
    answer.append(gcd)
    
    answer.append((n*m)//gcd)
    
    return answer