def solution(polynomial):
    nx = 0 
    n = 0
    
    for num in polynomial.split(' + '):
        if 'x' in num:
            nxn = num.replace('x','')
            nx += int(nxn) if nxn else 1
        else:
            n += int(num)
            
    result = []
    
    if nx > 0:
        if nx == 1:
            result.append("x") 
        else:
            result.append(f"{nx}x") 
            
    if n > 0:
        result.append(str(n))
        
    return " + ".join(result)