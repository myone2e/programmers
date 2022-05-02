n = 5 # 5개의 데이터 개수
data = [n*10 for n in range(1, 6)]

# Prefix Sum 계산 O(N+M) , N: 데이터 개수 / M: 쿼리 개수
summary = 0
prefix_sum = [0]
for i in data:
    summary += i
    prefix_sum.append(summary)
    
print(prefix_sum)

# Inverval Sum 계산
left = 3
right = 4
print(prefix_sum(right) - prefix_sum(left - 1))