def solution(s):
    answer = ''
    dic = {}
    
    for char in s:
        dic[char] = dic.get(char, 0) + 1
            
    result = sorted([k for k, v in dic.items() if v == 1])
    
    return "".join(result)