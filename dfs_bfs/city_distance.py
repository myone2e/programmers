from collections import deque
n, m, k, x = map(int, input().split()) # 도시, 도로, 거리, 출발점

graph = [[] for _ in range(n+1)]

for _ in range(m): # 간선의 갯수만큼
    start, end = map(int, input().split())
    graph[start].append(end) # 거리는 1로 가정
    
distance = [-1] * (n+1)
distance[x] = 0 # 출발 도시 

q = deque([x])
while q:
    now = q.popleft()
    for next in graph[now]:
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            q.append(next)

flag = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        flag = True
if flag == False:
    print(-1)