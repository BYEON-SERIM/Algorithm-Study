def solution(s):
    arr = list(s)
    
    arr = sorted(arr, reverse=True)
    
    return "".join(arr)