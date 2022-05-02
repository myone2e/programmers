n, m = map(int, input().split()) # 데이터 개수, 찾고자 하는 합

arr = list(map(int, input().split()))

s = arr[0]
i, j = 0, 0
min_len = 10000001

while True:
    if s >= m:
        s -= arr[i]
        min_len = min(min_len, j - i + 1) # 1,1 도 1이 나와야 함 & 1~2도 2
        i += 1
    else:
        j += 1
        if j == n:
            break
        s += arr[j]
        
print(min_len) if min_len!= 10000001 else print(0)