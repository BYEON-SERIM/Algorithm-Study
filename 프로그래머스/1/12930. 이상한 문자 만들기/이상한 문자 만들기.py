def solution(s):
    answer = []
    
    for word in s.split(' '):
        wd = ''
        for i in range(len(word)):
            if i%2==0:
                wd += word[i].upper()
            else:
                wd += word[i].lower()
                
        answer.append(wd)
        
    return ' '.join(answer)