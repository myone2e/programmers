expression = "100-200*300-500+20"

from itertools import permutations
def solution(expression):
    answer = 0
    cand = ['+','-','*']
    
    perms = list(map(list, permutations(cand))) ## 중요 스킬

    for p in perms: # p가 하나의 순열
        new = []
        first = expression.split(p[0]) # 첫 우선순위 연산자를 기준으로 나눔 (first: list)

        for part in first: # list 원소 하나씩
            second = part.split(p[1]) # 다시 두번째 우선순위 연산자로 나누고 (second: list)
            second = [str(eval(x)) for x in second] # 마지막 연산자 연산 실행
            new.append(p[1].join(second)) # 두번째 연산자로 다시 붙이고

        new=[str(eval(x)) for x in new] # 두번째 연산자 실행
        result=abs(eval(p[0].join(new))) # 첫번째 연산자 실행

        if result > answer:
            answer = result
    return answer
        
    
    