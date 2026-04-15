def solution(price, money, count):
    answer = 0

    total_price = 0 
        
    for i in range (1,count+1):
        total_price += i*price
        
    if total_price - money > 0:
        return total_price - money
    else:
        return 0
    