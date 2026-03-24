def solution(x):
    answer = True
    
    sumNum = []
    
    for num in str(x):
        sumNum.append(int(num))
    
    
    return True if x % sum(sumNum) == 0 else False