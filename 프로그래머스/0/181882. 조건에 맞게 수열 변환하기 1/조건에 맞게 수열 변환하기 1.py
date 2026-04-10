def solution(arr):
    answer = []
    
    for n in arr:
        if n%2 == 0 and n >= 50:
            answer.append(n/2)
        elif n%2 != 0 and n < 50:
            answer.append(n*2)
        else:
            answer.append(n)
            
    return answer