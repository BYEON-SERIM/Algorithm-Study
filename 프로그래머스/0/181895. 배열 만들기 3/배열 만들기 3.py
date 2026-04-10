def solution(arr, intervals):
    answer = []
    
    for ran in intervals:
        
        a = ran[0]
        b = ran[1] +1
        
        answer.extend(arr[a:b])
    
    return answer