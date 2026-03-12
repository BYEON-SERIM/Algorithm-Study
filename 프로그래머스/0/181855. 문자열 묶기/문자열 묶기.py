def solution(strArr):
    
    map = {}
    
    for char in strArr:
        if map.get(len(char)):
            map[len(char)] +=1
        else :
            map[len(char)] =1
    
    return max(map.values())