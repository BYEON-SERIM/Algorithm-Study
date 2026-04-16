def solution(rank, attendance):
    arr = sorted([(r, i) for i, (r, a) in enumerate(zip(rank, attendance)) if a])
    
    a, b, c = arr[0][1], arr[1][1], arr[2][1]
    
    return 10000 * a + 100 * b + c