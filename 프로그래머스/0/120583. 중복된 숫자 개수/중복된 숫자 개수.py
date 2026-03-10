def solution(array, n):
    answer = 0
    
    for ch in array:
        if(ch == n):
            answer += 1
    
    return answer