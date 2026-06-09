def solution(s, n):
    result = ""
    
    for c in s:
        if c == " ": # 공백은 그대로 추가
            result += " "
        elif c.isupper(): # 대문자일 경우
            # 'A'의 아스키 번호(65)를 뺀 후 n을 더하고, 
            # 26으로 나눈 나머지를 구해 알파벳 범위를 넘지 않게 함
            new_c = chr((ord(c) - ord('A') + n) % 26 + ord('A'))
            result += new_c
        elif c.islower(): # 소문자일 경우
            # 'a'의 아스키 번호(97)를 기준으로 계산
            new_c = chr((ord(c) - ord('a') + n) % 26 + ord('a'))
            result += new_c
            
    return result