n, m = map(int, input().split()) # row, col
data = [] # 초기 맵
temp = [[0]*m for _ in range(n)] # 벽 설치하는 맵

for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# 바이러스 퍼지도록 하는 dfs
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if temp[nx][ny] == 0: # 해당 위치에 바이러스 배치하고 다시 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)

# DFS를 이용해 벽을 설치하면서, 매번 안전 영역의 크기를 계산
def dfs(cnt):
    global result
    # 울타리가 3개 설치된 경우 => 채우고, 전파하고, 점수 계산
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] == data[i][j]
                
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
        # 안전 영역의 최대값 계산
        result = max(result, get_score)
        return # 점수까지 계산하고 종료
    
    # 3개가 아니라면 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0: # 하나 설치
                data[i][j] = 1
                cnt += 1
                dfs(cnt) # 그리고 3 개 될때까지 반복 (새로운 벽 있는 상태에서!)
                data[i][j] = 0 # 알렉스가 돌려놓으라는 거
                cnt -= 1
dfs(0) # 벽 없는 상태로 시작
print(result)
    
        