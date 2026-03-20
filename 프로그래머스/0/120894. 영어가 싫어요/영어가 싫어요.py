def solution(numbers):
    englishToNum = {
        "zero" : "0", "one" : "1", "two" : "2", "three": "3", "four": "4", "five": "5",
        "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"
    }
    
    temp_str = numbers
    
    for en, num in englishToNum.items():
        temp_str = temp_str.replace(en, num)  
    
    
    return int(temp_str)