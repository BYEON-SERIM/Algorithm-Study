def solution(str_list, ex):
    answer = ''
    return "".join([str for str in str_list if ex not in str])