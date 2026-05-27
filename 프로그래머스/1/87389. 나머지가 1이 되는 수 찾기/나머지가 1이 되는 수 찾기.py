def solution(n):
    answer = 3

    for i in range(1,n):
        if n%i == 1:
            return i
