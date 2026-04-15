def solution(code):
    answer = ''
    
    mode = 0
    
    for i, ch in enumerate(code):
        if mode == 0:
            if ch != "1":
                if i%2 == 0:
                    answer += ch
            else:
                mode = 1     
        else:           
            if ch != "1":
                if i%2 != 0:
                    answer += ch
            else:
                mode = 0      
    
    return answer if len(answer) != 0 else "EMPTY"