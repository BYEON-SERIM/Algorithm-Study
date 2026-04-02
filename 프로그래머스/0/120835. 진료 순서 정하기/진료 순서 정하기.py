def solution(emergency):
    sorted_list = sorted(emergency, reverse=True)
    
    return [sorted_list.index(i) +1 for i in emergency]