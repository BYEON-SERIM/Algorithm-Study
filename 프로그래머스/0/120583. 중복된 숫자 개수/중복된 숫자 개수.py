def solution(array, n):
    answer = 0
    
    for ch in array:
        if(ch == n):
            answer += 1
    
    # answer = array.count(n)    
    
    return answer