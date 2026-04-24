def solution(t, p):
    answer = 0
    
    arr = []

    for i in range(0,len(t) - len(p) + 1):
        word = t[i:i+len(p)]
        arr.append(int(word))
        
    return sum(1 for num in arr if num <= int(p))