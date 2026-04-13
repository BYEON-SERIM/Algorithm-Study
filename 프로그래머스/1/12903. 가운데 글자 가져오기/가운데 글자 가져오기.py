def solution(s):
    answer = ''
    
    if len(s)%2 == 0:
        index = len(s)//2
        answer = s[index-1:index+1]
    else:
        index = len(s)//2
        answer = s[index]
    
    return answer