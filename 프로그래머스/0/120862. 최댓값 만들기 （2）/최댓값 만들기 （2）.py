import math 

def solution(numbers):
    sortedNumber = sorted(numbers)
    
    return max(sortedNumber[-1]*sortedNumber[-2], sortedNumber[0]*sortedNumber[1])