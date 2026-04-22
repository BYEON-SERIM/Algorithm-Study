def solution(n):
    i = 2
    answer = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            answer.append(i)
    if n > 1:
        answer.append(n)
        
    return list(dict.fromkeys(answer))