def solution(a, b, n):
    answer = 0
    
    while(n>=a):
        new_coke = (n//a) * b  #새로 받을 콜라
        answer += new_coke
        
        n = new_coke + (n%a)
        
    return answer