def solution(intStrs, k, s, l):
    answer = []
    
    for num in intStrs:
        strToNum = num[s:s+l]
        
        if int(strToNum) > k:
            answer.append(int(strToNum))
    
    return answer