def solution(array):
    # 1. 숫자의 개수를 세는 딕셔너리 만들기
    count = {}
    for num in array:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
            
    # 2. 가장 많이 등장한 횟수(max_count) 구하기
    max_count = max(count.values())
    
    # 3. 최빈값을 가진 숫자가 몇 개인지 확인
    mode_list = []
    for key, value in count.items():
        if value == max_count:
            mode_list.append(key)
            
    # 4. 결과 반환
    if len(mode_list) > 1:
        return -1
    else:
        return mode_list[0]