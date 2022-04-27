import heapq
import sys

input = sys.stdin.readline

n = int(input())
data = []

for i in range(n):
    k = int(input())
    if k != 0:
        heapq.heappush(data, (abs(k), k))
    else:
        if not data: # heap is empty
            print(0)
        else:
            print(heapq.heappop(data)[1]) # 원래 값을 꺼낸다