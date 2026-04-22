def solution(s):
    answer = [ str.capitalize() for str in s.split(' ')]
             
    return ' '.join(answer)