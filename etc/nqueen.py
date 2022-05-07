import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
# row 가 스택!!!!!
row = [0] * n # 몇 열에 놓을 것인가 즉, idx가 행 넘버
# # row[i] = j < = > 퀸을 [i, j] 위치에 놓겠다

# x가 열 넘버
def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            # 같은 열에 퀸 or # 대각에 퀸 (행 차이, 열 차이 절대값이 같다. 대각이라서) 
            return False
    return True

def n_queens(x):
    global cnt
    if x==n: # 끝까지 왔다면 
        cnt += 1
        return

    else:
        for i in range(n): # x행의 모든 경우의 수에 대해
            row[x] = i # [x, i] 에 퀸을 놓겠다
            if is_promising(x): # [x, i] 가 유망하다면
                n_queens(x+1) # 다음으로 고

n_queens(0)
print(cnt)
    