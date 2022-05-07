info = [0,0,1,1,1,0,1,0,1,0,1,1]	
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]


def solution(info, edges):
    def next_nodes(v):
        temp = []
        for edge in edges:
            p, c = edge[0], edge[1] # 부모 자식
            if v == p: # 부모와 일치: 해당하는 길이다
                temp.append(c)
        return temp

    def dfs(sheep, wolf, current, path): # current: 시작점 / path에 연결된 애들 Next node 함수로 넣으면서 진행
        # 지금 노드 뭔지 확인
        if info[current] == 1: # 늑대라면
            wolf += 1
        else:
            sheep += 1

        # 늑대가 다 잡아먹었으면 끝
        if sheep <= wolf:
            return 0
        # 임시로 대입
        max_sheep = sheep
        for p in path:
            for n in next_nodes(p): # 연결된 다음 길에서
                if n not in path: 
                    path.append(n) # 없으면 넣고
                    max_sheep = max(max_sheep, dfs(sheep, wolf, n, path)) # 한 번 더 조지고
                    path.pop() # 백트래킹
        return max_sheep
    answer = dfs(0, 0, 0, [0])
    return answer