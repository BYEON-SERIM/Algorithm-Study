def solution(numlist, n):
    answer = []
    
    dic = {}
    
    for num in numlist:
        dic[num] = abs(n-num)
    
    sorted_dic = sorted(dic.items(), key=lambda x:(x[1],-x[0]))
    
    return  [item[0] for item in sorted_dic]