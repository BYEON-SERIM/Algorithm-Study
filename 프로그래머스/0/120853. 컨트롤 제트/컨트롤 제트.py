def solution(s):
    stack = []
    
    for n in s.split():
        if n == "Z":
            stack.pop()
        else:
            stack.append(int(n))
            
    return sum(stack)