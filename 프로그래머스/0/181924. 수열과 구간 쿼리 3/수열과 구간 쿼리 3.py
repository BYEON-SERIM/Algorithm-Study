def solution(arr, queries):
    answer = arr
    
    for ran in queries:
        a = ran[0]
        b = ran[1]
        
        x = arr[a]
        y = arr[b]
        
        answer[a] = y
        answer[b] = x
    
    return answer