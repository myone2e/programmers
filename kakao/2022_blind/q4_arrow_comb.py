# 만약, k(k는 1~10사이의 자연수)점을 어피치가 a발을 맞혔고 라이언이 b발을 맞혔을 경우 더 많은 화살을 k점에 맞힌 선수가 k 점을 가져갑니다. 
# 단, a = b일 경우는 어피치가 k점을 가져갑니다. k점을 여러 발 맞혀도 k점 보다 많은 점수를 가져가는 게 아니고 k점만 가져가는 것을 유의하세요. 
# 또한 a = b = 0 인 경우, 즉, 라이언과 어피치 모두 k점에 단 하나의 화살도 맞히지 못한 경우는 어느 누구도 k점을 가져가지 않습니다.
# 라이언이 가장 큰 점수 차로 이기는 경우를 return
n = 5
info = [2,1,1,1,0,0,0,0,0,0,0] # 10점 2개, 9점 1개,.... 0점 0개 (len = 11) - 어피치 점수


from itertools import combinations_with_replacement

def solution(n, info):
    answer = [0 for _ in range(11)]
    win = False
    max_num = 0   # 라이언이 이길때 가장큰 점수 차이
    # 1. 중복 조합을 이용해 라이언의 점수를 만든다.
    # [(0, 0, 0, 0, 0), (0, 0, 0, 0, 1), (0, 0, 0, 0, 2) .... (0, 0, 0, 0, 10), (0, 0, 0, 1, 1),, ...
    # .. (9, 10, 10, 10, 10), (10, 10, 10, 10, 10)]
    for res in list(combinations_with_replacement(range(0, 11), n)): # 대상, 갯수
        now = [0 for _ in range(11)]
        for r in res:
            now[10 - r] += 1
        lion = 0
        peach = 0
        # 2. 라이언 점수와 어피치 점수 비교한다.
        for i, (l, p) in enumerate(zip(now, info)): # zip으로 튜플로 원소마다 묶어줌
            if l == p == 0:
                continue
            if p >= l:
                peach += (10 - i)
            elif l > p:
                lion += (10 - i)
        # 3. 총 점수를 비교해 라이언이 큰 경우 결과를 업데이트 해준다.
        if lion > peach:
            win = True # 1번 이기면 계속 True
            if (lion - peach) > max_num:
                max_num = lion - peach
                answer = now
    if not win:
        return [-1]
    return answer

# [0,2,2,0,1,0,0,0,0,0,0]