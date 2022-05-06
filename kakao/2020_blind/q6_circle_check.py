from itertools import permutations

def solution(n, weak, dist):
    # 길이를 2배로 늘려서 원형을 일자로
    len_weak = len(weak)
    for i in range(len_weak):
        weak.append(weak[i] + n)
    
    answer = len(dist) + 1 # 각 지점마다 투입이 최악 / 마지막에 dist보다 길면 -1 할라고 +1 
    
    # 0부터 len_weak - 1까지의 위치를 각각 시작점으로 설정
    for start in range(len_weak):
        # 모든 경우에 수에 대해
        for friends in list(permutations(dist, len(dist))):
            cnt = 1 # 투입도 1로 시작
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[cnt - 1]
            
            # 시작점부터 모든 취약한 지점을 확인
            for idx in range(start, start + len_weak):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[idx]:
                    cnt += 1 # 새로운 친구를 투입
                    if cnt > len(dist): # 더 투입이 불가능하다면 종료
                        break
                    position = weak[idx] + friends[cnt - 1]
            answer = min(answer, cnt) # 최솟값 계산
    if answer > len(dist):
        return -1
    return answer