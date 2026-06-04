def solution(arr):
    
    answer = []
    
    for i in range(0,len(arr)):
        if arr[i] != arr[i-1] or len(answer) == 0:
            answer.append(arr[i])
    
    return answer