
tmp1 = [[i for i in range(n)] for n in range(6,10)] # 바깥꺼가 먼저돈다
print(tmp1)
# [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7, 8]]

tmp1 = [tuple([i for i in range(n)]) for n in range(6,10)] # 리스트에 튜플씌우면 바로 튜플됨!!
print(tmp1)
# [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7, 8]]

tmps = []
for n in range(6,10):
    tmpss = [i for i in range(n)]
    tmps.append(tmpss)
print(tmps)
# [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7, 8]]

tmp2 = []
for n in range(6,10):
    tmp3 = [] # 이거 없으면 일렬로 들어감
    for i in range(n):
        tmp3.append(i)
    tmp2.append(tmp3)

print(tmp2) 
# [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7, 8]]

relation = [["100","ryan","music","2"],
             ["200","apeach","math","2"],
             ["300","tube","computer","3"],
             ["400","con","computer","4"],
             ["500","muzi","music","3"],
             ["600","apeach","music","2"]]
from itertools import combinations
n_row = len(relation)
n_col = len(relation[0])
comb = []
for i in range(1, n_col+1):
    comb.extend(combinations(range(n_col), i)) # possible combinations # 리스트 등이 원소가 풀어져서 들어감

for i in comb:
    tmp = []
    for item in relation:
        tmp.append(tuple([item[key] for key in i])) 
    print(tmp)
    
print('---------------')
tmp = [tuple([item[key] for key in i]) for item in relation] # 바깥꺼가 먼저 돈다  
print(tmp)
