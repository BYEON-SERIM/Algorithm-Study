def solution(arr):

    l = len(arr)
    target = 1
    
    while target <l:
        target *= 2
        
    zeroCnt = target - l
    
    return arr + [0]*zeroCnt