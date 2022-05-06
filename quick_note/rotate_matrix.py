# 90 degrees
def rotate_matrix(mat):
    row_len = len(mat)
    col_len = len(mat[0])
    
    res = [[0] * row_len for _ in range(col_len)] ## 행 열 숫자도 바껴야해서
    
    for r in range(row_len):
        for c in range(col_len):
            res[c][row_len - 1 - r] = mat[r][c]
            
    return res