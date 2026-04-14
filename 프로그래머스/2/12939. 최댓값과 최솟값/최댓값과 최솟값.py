def solution(s):  
    arr = [int(x) for x in s.split(' ')]
    
    maxNum = max(arr)
    minNum = min(arr)
    
    answer = str(minNum) + ' ' + str(maxNum)
    
    return answer