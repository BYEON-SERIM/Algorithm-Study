def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        candidates = []
        
        for num in arr[s:e+1]:
            if num > k:
                candidates.append(num)
        
        if candidates:
            answer.append(min(candidates))
        else:
            answer.append(-1)
    
    return answer