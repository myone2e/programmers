def solution(n, s, a, b, fares):
    
    INF = 1e9

    graph = [[INF] * (n+1) for _ in range(n+1)]
    # 자기 자신 초기화
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i==j:
                graph[i][j] = 0
    for fare in fares:
        i, j, cost = fare[0], fare[1], fare[2]
        graph[i][j] = cost
        graph[j][i] = cost

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j] , graph[i][k] + graph[k][j]) 

    distance = INF
    # 경유 지점 탐색
    for t in range(1, n+1):
        temp = graph[s][t] + graph[t][a] + graph[t][b] # 같이 + A 혼자 + B 혼자
        distance = min(temp, distance)

    return distance


