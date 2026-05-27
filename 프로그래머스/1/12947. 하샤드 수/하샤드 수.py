def solution(x):
    xStr = [int(num) for num in str(x)]
    xSum = sum(xStr)
    
    return True if x%xSum == 0 else False