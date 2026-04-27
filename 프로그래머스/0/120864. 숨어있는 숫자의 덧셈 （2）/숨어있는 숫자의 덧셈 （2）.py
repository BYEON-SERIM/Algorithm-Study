def solution(my_string):
    answer = []
    
    for ch in my_string:
        if ch.isalpha():
            my_string = my_string.replace(ch, ' ')

    answer = my_string.split()        
            
    return sum([int(x) for x in answer])