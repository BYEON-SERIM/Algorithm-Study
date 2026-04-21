def solution(s):
    arr = []
    
    for ch in s:
        arr.append(ch)
    
    arr.sort(reverse=True)
    
    return "".join(arr)