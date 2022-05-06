# 90 degrees
def rotate_matrix(mat):
    row_len = len(mat)
    col_len = len(mat[0])
    
    res = [[0] * row_len for _ in range(col_len)] ## 행 열 숫자도 바껴야해서
    
    for r in range(row_len):
        for c in range(col_len):
            res[c][row_len - 1 - r] = mat[r][c]
            
    return res

# 3배로 늘린 자물쇠의 중간 부분이 모두 1인지 확인 (모두 1 = > 열림)
def check(new_lock):
    lock_length = len(new_lock) // 3
    # 3배라서 len ~ 2len 확인
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 정중앙 부분만 1로 변경
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j] 
    
    for rotation in range(4):
        key = rotate_matrix(key) # 열쇠 회전 (1번씩)
        for x in range(n*2):
            for y in range(n*2):
                # 자물쇠에 열쇠를 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                
                if check(new_lock) == True:
                    return True
                
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False