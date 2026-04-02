def solution(my_string):
    answer = my_string.split(" ")
    
    
    result = int(answer[0])
    
    for i in range(1, len(answer), 2):
        oper = answer[i]
        num = answer[i+1]
        
        if oper == "+":
            result += int(num)
        else:
             result -= int(num)
    
    return result