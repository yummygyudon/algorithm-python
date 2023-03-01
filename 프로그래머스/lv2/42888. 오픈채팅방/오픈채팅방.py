"""
닉넴 변경 방법
    1. 나간 후, 새로운 닉넴으로 들어가기
    2. 나가지 않고 채팅방에서 닉넴 변경하기
중복 아이디 허용
"""
ACCOUNT = dict()

def solution(record):
    global ACCOUNT
    record = [e.split(" ") for e in record]
    for log in record :
        if log[0] == 'Enter' :
            # logElements = list(log.split(" "))
            changeNicknameOf(log[1], log[2])
        elif log[0] == 'Change' :
            # logElements = list(log.split(" "))
            changeNicknameOf(log[1], log[2])
    # print(ACCOUNT)
    answer = []
    for log in record :
        if log[0] == 'Enter' :
            answer.append("%s님이 들어왔습니다."%(ACCOUNT.get(log[1])))
        elif log[0] == 'Leave' :
            answer.append("%s님이 나갔습니다."%(ACCOUNT.get(log[1])))
    
    return answer

def enter(uid, uname) :
    global ACCOUNT
    if uid not in ACCOUNT.keys() :
        # print("삽입")
        ACCOUNT[uid] = uname
        
def changeNicknameOf(uid, newName) :
    global ACCOUNT
    # print("교체 : ",ACCOUNT.get(uid)," to ", newName )
    ACCOUNT[uid] = newName
