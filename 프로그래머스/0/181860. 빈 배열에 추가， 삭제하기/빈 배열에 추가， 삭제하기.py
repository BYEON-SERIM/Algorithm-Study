def solution(arr, flag):
    answer = []
    
    for num, fl in zip(arr, flag):
        if fl:
            for _ in range(num*2):
                answer.append(num)
        else:
            for _ in range(num):            
                answer.pop()
            
    return answer