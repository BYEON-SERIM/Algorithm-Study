def solution(arr, k):
    answer = []
    
    answer = list(dict.fromkeys(arr))
    
    return answer + [-1]*(k-len(answer)) if k>len(answer) else answer[0:k]