from collections import deque

def bfs(n, info):    
    res = []
    q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
    # focus: 0 (0번째 = 10점 과녁에 쏘겠다) #arrow: [0...0]: 현재 과녁 상황
    maxGap = 0
    
    while q:
        focus, arrow = q.popleft()
        
        if sum(arrow) == n:  # 종료조건 1) 화살 다 쏜 경우
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            # 화살을 다 쏘고 종료된 경우 점수를 확인
            if apeach < lion:  # 라이언이 이기면
                gap = lion - apeach
                if maxGap > gap:
                    continue
                if maxGap < gap:
                    maxGap = gap  # 최대점수차 갱신
                    res.clear() # 이전에 쓰던 거를 비우고
                res.append(arrow)  # 최대점수차를 내는 화살 조합 저장
        
        elif sum(arrow) > n:  # 종료조건 2) 화살 더 쏨. 계속 1발 씩 더 쏘다가 한도 초과
            continue
        
        elif focus == 10:  # 종료 조건 3) 화살을 덜 쏜 경우 (극단적으로 계속 0발만 쏘는 상황. 0점 과녁까지 옴)
            tmp = arrow.copy()
            tmp[focus] = n - sum(tmp) # 남은거 0점에 몰고
            q.append((-1, tmp)) # 화살을 다 쐈으니 focus는 이제 필요 없으므로 아무 값이나 넣어준다.
        
        else:  # 화살 쏘기
            tmp = arrow.copy()
            tmp[focus] = info[focus]+1 # 어피치보다 1발 많이 쏘기
            q.append((focus+1, tmp))  # 다음 과녁으로 이동
            tmp2 = arrow.copy()
            tmp2[focus] = 0 # 쏘지 않기
            q.append((focus+1, tmp2))  # 다음 과녁으로 이동
    return res

def solution(n, info):
    winList = bfs(n, info)
    
    if not winList:
        return [-1]
    elif len(winList) == 1:
        return winList[0]
    else:
        return winList[-1]

# 우리는 focus를 도입해 높은 점수부터 화살을 쏘도록 문제를 풀었으므로, 보다 낮은 점수를 맞힌 경우가 나중에 append되었음을 알 수 있다.
# 가장 낮은 점수를 맞힌 경우는 winList의 마지막 원소가 된다. 따라서 winList[-1] 리턴