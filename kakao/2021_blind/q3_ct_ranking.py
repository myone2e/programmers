
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

from itertools import combinations
from collections import defaultdict  # 이게 뭐꼬
def solution(info, query):
    answer = []
    # 조합: 점수
    info_dict = defaultdict(list)
    # java :[80,150] , 'javapizza': [150]...

    # 1.1 하나의 Info에 대한 경우의 수 16개 (2^4: - or char) for each person
    for i in info:
        row = i.split()
        info_keylist = row[:-1]
        info_value = int(row[-1])
        for j in range(5): # 하나의 info에 대한 경우의 수 16개
            for c in combinations(info_keylist, j):
                info_key = ''.join(c)
                info_dict[info_key].append(info_value)

    for key in info_dict.keys():
        info_dict[key].sort() # 점수 정렬
        #print(info_dict)

    # 2. 쿼리 정리
    for q in query:
        row = q.split(' ')
        q_score = int(row[-1])
        query = row[:-1]

        # and 제거 (무조건 3개)
        while 'and' in query:
            query.remove('and')
        # - 제거
        while '-' in query:
            query.remove('-')
        query_key = ''.join(query)

        # 3. 쿼리에서 입력한 점수보다 큰 점수들의 갯수 구하기

        # 3.1 쿼리에 해당하는 점수 찾기 (해당되는 모든 사람들) ㄷ
        if query_key in info_dict:
            score_list = info_dict[query_key] # dict에서 뽑음

            # 3.2 쿼리보다 높은 점수 사람들 세기 : 이진 탐색
            if len(score_list) > 0:
                start = 0
                end = len(score_list) 
                while start < end: # 같아지면 끝나도록 !
                    mid = (start+end) // 2
                    if score_list[mid] >= q_score:
                        end = mid
                    else:
                        start = mid + 1

                answer.append(len(score_list) - start)
        # 쿼리에 이상인 스코어가 없을 때
        else:
            answer.append(0) 
    return answer

print(solution(info, query))