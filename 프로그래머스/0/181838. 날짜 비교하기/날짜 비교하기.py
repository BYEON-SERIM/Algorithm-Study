def solution(date1, date2):
    dateStr1 = int("".join(map(str, date1)))
    dateStr2 = int("".join(map(str, date2)))
    
    return 1 if dateStr1 < dateStr2 else 0