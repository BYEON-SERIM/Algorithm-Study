def solution(arr):
    answer = 0
    
    if len(arr) == 1:
        return [-1]
    
    minNum = min(arr)
    
    arr.remove(minNum)
    
    return arr