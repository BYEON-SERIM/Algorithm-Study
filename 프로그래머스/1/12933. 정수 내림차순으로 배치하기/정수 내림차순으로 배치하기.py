def solution(n):
    answer = 0
    
    numList = []
    
    for num in str(n):
        numList.append(num)
    
    reverseNum = sorted(numList, reverse=True)
    
    return int("".join(reverseNum))