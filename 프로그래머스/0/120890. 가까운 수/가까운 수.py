def solution(array, n):
    answer = 0
    
    dic={}
    
    for num in array:
        dic[num] = abs(n-num)
        
    min_key = min(dic, key=lambda k: (dic[k], k))
    
    
    return min_key