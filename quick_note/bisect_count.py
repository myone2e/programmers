from bisect import bisect_left, bisect_right

n, x = map(int, input().split())

nums = list(map(int, input().split()))

def count_by_range(array, left_value, right_value):
    idx_left = bisect_left(array, left_value)
    idx_right = bisect_right(array, right_value)
    return idx_right - idx_left

count = count_by_range(nums, x, x)
if count == None:
    print(-1)
else:
    print(count)