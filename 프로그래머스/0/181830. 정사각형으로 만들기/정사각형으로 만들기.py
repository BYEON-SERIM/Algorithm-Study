def solution(arr):

    row = len(arr)
    col = len(arr[0])
    
    n = max(row, col)
    
    answer = [[0] * n for _ in range(n)]
    
    for i in range(row):
        for j in range(col):
            answer[i][j] = arr[i][j]
            
    return answer