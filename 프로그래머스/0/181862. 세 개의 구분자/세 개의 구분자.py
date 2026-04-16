def solution(myStr):
    answer = []
    
    answer = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ')
    
    answer = answer.split()
    
    return answer if answer else ["EMPTY"]