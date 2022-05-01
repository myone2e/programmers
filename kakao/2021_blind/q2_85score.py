orders = ["XYZ", "XWY", "WXA"]

course = [2,3,4]
# 같은 두 글자 중에 가장 많이 언급된 메뉴였네요
# ad는 총 3번 주문 ab는 총 2번 주문 --> 동 길이일때는 가장 많이 주문된 것을 채택
from itertools import combinations

def solution(orders, course):
        
    alphas = []
    for i in orders:
        alphas.extend(list(i))
    temp = []
    for a in alphas:
        if a not in temp:
            temp.append(a)
    temp.sort()

    comb = []
    for i in course:
        comb.extend(combinations(temp, i))

    hash = dict()
    for i in comb:
        new = '' # 조합
        for k in i: # i 가 이미 알파벳 튜플
            new += k
        if new not in hash.keys():
            hash[new] = 0
        for s in orders: # s: 한 문자열 # new: 검사하는 대상
            if set(list(new)).issubset(set(list(s))): 
                hash[new] += 1

    # pos = {k:v for k,v in hash.items() if v != 0} 
    answer = []
    for c in course:
        tmp = []
        max_val = 2
        for k,v in hash.items():
            if v < 2:
                continue
            elif len(k) == c and max_val == v:
                tmp.append(k)
            elif len(k) == c and max_val < v:
                tmp.clear()
                tmp.append(k)
                max_val = v
        answer.extend(tmp)
        answer.sort()
    return answer

solution(orders, course)