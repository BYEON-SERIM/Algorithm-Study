def solution(arr, divisor):

    arr = [n for n in arr if n%divisor == 0]
    
    return sorted(arr) if len(arr) else [-1]