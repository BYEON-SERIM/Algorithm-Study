def solution(my_str, n):
    answer = []
    
    l = len(my_str)
    
    for i in range(0,l,n):
        str = my_str[i:i+n]
        answer.append(str)
    
    return answer