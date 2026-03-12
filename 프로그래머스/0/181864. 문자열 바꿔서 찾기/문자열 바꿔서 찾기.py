def solution(myString, pat):
    reverse = ""
    
    for char in myString:
        if char == "A":
            reverse += "B"
        else:
            reverse += "A"
    
    return 1 if pat in reverse else 0