def solution(n):
    return sum( num ** 2 for num in range (2, n+1,2)) if n%2 == 0 else sum(num for num in range(1, n+1,2))