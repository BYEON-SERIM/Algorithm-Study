def solution(myString, pat):
    answer = ''
    
    index = myString.rfind(pat)
    index = index+len(pat)
    
    return myString[:index]