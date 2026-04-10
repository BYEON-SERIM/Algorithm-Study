def solution(my_strings, parts):
    answer = ''
    
    for word, ran in zip(my_strings, parts):
        a = ran[0]
        b = ran[1] + 1
        
        answer += word[a:b]
    
    return answer