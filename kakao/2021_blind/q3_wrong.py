info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
info = [s.split() for s in info]

query = [s.split() for s in query]

for i in range(len(query)):
    while 'and' in query[i]:
        query[i].remove('and')

answer = []
idx_lst = [0,1,2,3] # 정수 필터링 뺀 index
for q in query: # 쿼리를 돌린다
    cnt = 0
    tmp = [p for p in info if int(p[-1])>=int(q[-1])] # 점수는 무조건 들어오니까 필터링
    q.pop(-1)
    while '-' in q:
        remove_idx = q.index('-')
        q.pop(remove_idx)
        # ['python', 'frontend', 'senior'] 이런 식으로 남아있음
    if q == []: # 다 - 라면 점수 만족시키는 애들만큼 +
        cnt += len(tmp)
        answer.append(cnt)
        break
    for k in info:
        if set(q).issubset(set(k)):
            cnt += 1
    answer.append(cnt)
print(answer)
    
    
        
    
        
    
