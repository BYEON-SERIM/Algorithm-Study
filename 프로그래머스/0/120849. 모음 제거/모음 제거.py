def solution(my_string):
    answer = ''
    
    aeiou = ["a", "e", "i", "o", "u"]
    
    for char in my_string:
        if char in aeiou:
            answer += ""
        else:
            answer += char
                
    return answer