import heapq
import sys

input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    k = int(input())
    if k != 0:
        heapq.heappush(data, -k) # 부호 바꿔서 넣고
    else:
        try:
            print(-heapq.heappop(data)) # 뽑을 때도 부호 바꿔서
        except:
            print(0)