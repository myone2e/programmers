import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int,input().split()) # n x n 맵, k까지 종류

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
    
S, X, Y = map(int,input().split()) 


dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 0 이 아닌 지점 (virus 개념)을 모두 넣고 시작
data = []
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j)) # 2번째가 시간을 의미 => 시간을 같이 넣어주는 스킬!
data.sort()
q = deque(data)

def bfs(graph):
    while q:
        virus, s, x, y = q.popleft()
        if s == S:
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N: # 맵을 나가면 무시
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus,s+1, nx, ny))
    return graph

box = bfs(graph)

print(box[X-1][Y-1])
                