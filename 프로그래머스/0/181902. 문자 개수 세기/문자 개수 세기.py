def solution(my_string):
    answer = [0]*52
    
    for c in my_string:
        
        if c.isupper():
            idx = ord(c) - 65
            answer[idx] += 1
        else:
            idx = ord(c) - ord('a') + 26
            answer[idx] += 1

    return answer