def solution(my_string, indices):
    answer = ''
    
    for i, char in enumerate(my_string):
        if i in indices:
            answer += ''
        else:
            answer += char
    
    return answer