def solution(keyinput, board):
    x, y = 0, 0
    
    max_x = board[0] // 2
    max_y = board[1] // 2
    
    dic = {
        "up"    : [0, 1],
        "down"  : [0, -1],
        "left"  : [-1, 0],
        "right" : [1, 0]
    }
    
    for direc in keyinput:
        dx, dy = dic[direc]
        
        nx = x + dx
        ny = y + dy
        
        if -max_x <= nx <= max_x:
            x = nx
        if -max_y <= ny <= max_y:
            y = ny
            
    return [x, y]