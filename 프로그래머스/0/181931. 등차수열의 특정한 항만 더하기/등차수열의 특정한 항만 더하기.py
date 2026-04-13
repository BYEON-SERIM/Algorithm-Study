def solution(a, d, included):
    arrList = []
    
    nowNum = a
    
    for n in included:
        if n == True:
            arrList.append(nowNum)
        
        nowNum += d
    
    return sum(arrList)