N = 4
stages = [4,4,4,4]

def get_fail_rate(k, stages): # k 번째 스테이지
    not_cleard = 0
    reached = 0
    for i in stages:
        if i >= k:
            reached += 1
        if i == k:
            not_cleard += 1
    if reached == 0: # 분모 0 예외처리 조건 
        return 0
            
    return not_cleard/reached

def solution(N, stages):
    answer = []
    result = []
    for i in range(1, N+1):
        fail = get_fail_rate(i, stages)
        result.append([i, fail])
    result.sort(key = lambda x: x[1], reverse=True) # 실패율 내림차순으로 정렬
    for r in result:
        answer.append(r[0])
    return answer
        
print(solution(N,stages))

# result = [3,4,2,1,5]