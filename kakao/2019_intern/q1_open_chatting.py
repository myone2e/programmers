record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    answer = []
    people = dict()

    tmp = []
    for i in range(len(record)):
        tmp.append(list(record[i].split()))

    for cmd in tmp:
        if len(cmd) > 2: # 출입
            people[cmd[1]] = cmd[2]

    for r in record:
        if r.split()[0] == 'Enter':
            answer.append(people[r.split()[1]]+'님이 들어왔습니다.')
        elif r.split()[0] == 'Leave':
            answer.append(people[r.split()[1]]+'님이 나갔습니다.')
    return answer



#result = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]