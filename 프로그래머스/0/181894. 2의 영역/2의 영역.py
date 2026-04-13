def solution(arr):
    answer = []
    
    if 2 not in arr:
        return [-1]
    
    indexes = [i for i, val in enumerate(arr) if val == 2]
    
    if len(indexes) == 1:
        return [2]
    
    min_idx = min(indexes)
    max_idx = max(indexes)
    
    return arr[min_idx:max_idx+1]