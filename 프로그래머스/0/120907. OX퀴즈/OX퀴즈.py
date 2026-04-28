def solution(quiz):
    answer = []
    
    for m in quiz:
        arr = m.split(' ')
        
        if arr[1] == '+':
            if int(arr[0]) + int(arr[2]) == int(arr[4]):
                answer.append("O")
            else:
                answer.append("X")
        elif arr[1] == '-':
            if int(arr[0]) - int(arr[2]) == int(arr[4]):
                answer.append("O")
            else:
                answer.append("X")
    
    return answer