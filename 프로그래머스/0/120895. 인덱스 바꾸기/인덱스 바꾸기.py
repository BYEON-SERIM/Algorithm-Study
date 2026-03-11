def solution(my_string, num1, num2):
    answer = ''
    
    char1 = my_string[num1]
    char2 = my_string[num2]
    
    for i, char in enumerate(my_string):
        if i == num1:
            answer += char2
        elif i == num2:
            answer += char1
        else:
            answer += char
    
    return answer