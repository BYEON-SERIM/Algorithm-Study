def solution(s):
    answer = []
    
    for word in s.split(' '):
        newWord = ''    
        for i in range(len(word)):
            if i%2 == 0:
                newWord += word[i].upper()
            else:
                newWord += word[i].lower()
                
        answer.append(newWord)
    
    return " ".join(answer)