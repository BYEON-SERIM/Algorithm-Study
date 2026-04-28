from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    counts = Counter(tangerine)
    
    for size, cnt in counts.most_common():
        k -= cnt
        answer += 1
        
        if k <= 0:
            break
    
    return answer