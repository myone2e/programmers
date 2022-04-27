import sys
input = sys.stdin.readline

# Dynamic programming problem
# Time limit using bruteforce O(n^2)
# dp[i] represents the largest sum of all subarrays ending with index i
# => then its value should be the larger one between 
# nums[i] (without using prefix) and dp[i-1] + nums[i] (using prefix with largest sum plus current number):

def maxSubArray(nums):
        l = len(nums)
        if l == 1:
            return nums[0]

        dp = [0] * (l+1)
        dp[0] = nums[0]
        max_sum = dp[0] # 맨 처음 하나만 고르는 경우
        for i in range(1, l):
            dp[i] = max(dp[i-1] + nums[i], nums[i]) # 이전까지의 최고합을 가져가거나, 새로 시작하거나
            if dp[i] > max_sum:
                max_sum = dp[i]
        return max_sum

T = int(input()) # 테스트 케이스 수
for _ in range(T):
    n = int(input())
    arr = list(map(int,input().split()))
    print(maxSubArray(arr))
    