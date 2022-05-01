orders = ["XYZ", "XWY", "WXA"]

course = [2,3,4]
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    # 메뉴 갯수 하나씩 돌면서
    for c in course:
        combinationArray=[]
        for order in orders:
            combinationArray+=list(combinations(sorted(order),c)) # 주문이 알파벳 순서로 안들어옴 & 리스트만들고 하나씩 뽑음
        combinationArray=Counter(combinationArray)
        # counter는 array를 받아서 갯수를 새주는 역할. 딕셔너리같이 만들어줌!
        # c = 3: Counter({('X', 'Y', 'Z'): 1, ('W', 'X', 'Y'): 1, ('A', 'W', 'X'): 1})
        
        answer+=[''.join(k) for k, v in combinationArray.items() if v == max(combinationArray.values()) and v>1]
    
    return sorted(answer)

solution(orders,course)