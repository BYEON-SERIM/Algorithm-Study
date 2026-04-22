from collections import Counter

def solution(a, b, c, d):
    counts = Counter([a, b, c, d])
    
    items = counts.most_common()
    
    cnt = len(items)
    
    if cnt == 1:
        p = items[0][0]
        return 1111*p
    elif cnt == 2:
        if items[0][1] == 3:
            p, q = items[0][0], items[1][0]
            return (10 * p + q) ** 2
        else:
            p, q = items[0][0], items[1][0]
            return (p + q) * abs(p - q)
    elif cnt == 3:

        q, r = items[1][0], items[2][0]
        return q * r 
    else:
        return min(a, b, c, d)
