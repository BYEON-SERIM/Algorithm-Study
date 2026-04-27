def solution(num, k):
    arr = [ int(num) for num in  str(num) ]
    
    return arr.index(k)+1 if k in arr else -1