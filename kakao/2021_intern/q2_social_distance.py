places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
from collections import deque
def solution(places):
    answer = []
    dist = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for line in places:
        graph = [[0]*len(line) for _ in range(len(line))]
        queue = deque()
        for i in range(5):
            for j in range(5):
                if line[i][j] == 'P': # Person
                    graph[i][j] = 1
                    queue.append((i,j))
                elif line[i][j] == 'X': # partition
                    graph[i][j] = -1
        dist = 1
        while queue and dist == 1:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx<0 or ny < 0 or nx >= 5 or ny >= 5:
                    continue
                
                if graph[nx][ny] == 1: # 옆자리에 사람이 있다면
                    dist = 0
                else: # 옆자리에 사람이 없다면 
                    if graph[nx][ny] == -1: # 벽이라면 무시
                        continue
                    else: # 비었다면
                        for j in range(4):
                            nx2 = nx + dx[j]
                            ny2 = ny + dy[j]
                            if nx2<0 or ny2 < 0 or nx2 >= 5 or ny2 >= 5: # 벽 넘어가면 무시
                                continue
                            if nx2 == x and ny2 == y: # 다시 돌아와도 무시
                                continue
                            if graph[nx2][ny2] == 1: # 또 사람이라면, 거리두기 false
                                dist = 0
        answer.append(dist)       

    return answer
# [1, 0, 1, 1, 1]