def solution(id_pw, db):
    answer = ''
    
    user_id = id_pw[0]
    user_pw = id_pw[1]
    
    for db_id, db_pw in db:
        if user_id == db_id:
            if user_pw == db_pw:
                return "login"
            else:
                return "wrong pw"
            
    return "fail"