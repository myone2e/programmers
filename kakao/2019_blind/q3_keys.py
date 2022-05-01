relation = [["100","ryan","music","2"],
             ["200","apeach","math","2"],
             ["300","tube","computer","3"],
             ["400","con","computer","4"],
             ["500","muzi","music","3"],
             ["600","apeach","music","2"]]

from itertools import combinations

def solution(relation):        
    n_row = len(relation)
    n_col = len(relation[0])

    comb = []
    for i in range(1, n_col+1):
        comb.extend(combinations(range(n_col), i)) # possible combinations # 리스트 등이 원소가 풀어져서 들어감

    # 유일성
    unique = []
    for i in comb: # i 는 가능한 조합 하나
        # item: 각 row  / key: 0,1,2.. / i 가능한 조합 튜플
        tmp = [tuple([item[key] for key in i]) for item in relation] # 바깥꺼가 먼저 돈다! => 튜플로 이루어진 리스트가 생성됨
        print(tmp)
        if len(set(tmp)) == n_row: # 유일성
            flag = True

            for x in unique:
                if set(x).issubset(set(i)): # 최소성 => unique안의 x가 i의 부분집합에 해당하는가
                    flag = False

            if flag:
                unique.append(i)
    return len(unique)
solution(relation)
# 학번, [이름, 전공]
