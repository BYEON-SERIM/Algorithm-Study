def solution(food):
    answer = []
    
    for i, n in enumerate(food):
        if i == 0:
            continue;
        else:
            answer += str(i)*(n//2)

    reAnswer = answer[::-1]
    
    answer.append('0')
    
    
    return "".join(answer+reAnswer)