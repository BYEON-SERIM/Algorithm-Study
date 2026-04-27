def solution(arr):
    answer = 0 
    
    while True:
        next_arr = []
        for n in arr:
            if n >= 50 and n % 2 == 0:
                next_arr.append(n // 2)
            elif n < 50 and n % 2 != 0:
                next_arr.append(n * 2 + 1)
            else:
                next_arr.append(n)

        if arr == next_arr:
            return answer
        
        arr = next_arr
        answer += 1