def solution(phone_number):
    answer = ''
    
    for i in range(1,len(phone_number) - 3):
        answer += "*"
    
    return answer + phone_number[-4:]