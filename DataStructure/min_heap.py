import heapq
import sys

input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    k = int(input())
    if k != 0:
        heapq.heappush(data, k)
    else:
        try:
            print(heapq.heappop(data))
        except:
            print(0)
        