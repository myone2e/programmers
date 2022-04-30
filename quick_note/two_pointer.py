n, m = 5, 5 # 5개의 데이터에서 합이 5인 구간의 갯수 찾기
data = [1,2,3,4,5]

result = 0
summary = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    while summary < m and end < n:
        summary += data[end]
        end += 1
    if summary == m:
        result += 1
    # start 옮길 때 마다 빼주기
    summary -= data[start]
    
print(result)