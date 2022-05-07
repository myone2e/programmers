import sys

n = int(sys.stdin.readline())

row = [0] * n # 몇 열에 놓을 것인가 즉, idx가 행 넘버
cnt = 0
visited = [False] * n

# x가 열 넘버
def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            # 같은 열에 퀸 or # 대각에 퀸 (행 차이, 열 차이 절대값이 같다. 대각이라서) 
            return False
    return True

def dfs(x):
    global cnt
    if x == n:
        cnt += 1
        return
    
    for i in range(n): # 다음 행을 탐색
        if visited[i]: # 같은 열에 퀸이 있으면
            continue
            
        row[x] = i # 없으면 [x, i] 에 퀸을 놔보고 (탐색해보고)
        
        if is_promising(x): # 유망하다면
            visited[i] == True # 고 (이 열에 있다고 마크)
            dfs(x+1)
            visited[i] = False # 내려갔다가 답이 아니면 싹 지우기 개념! 알렉스
dfs(0)
print(cnt)