def solution(my_string, n):
    answer = ''
    
   # for ch in my_string:
   #     answer += ch*n
    
    return "".join(ch*n for ch in my_string)