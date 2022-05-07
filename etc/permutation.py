class Solution:
    def permute(self, nums):
        results = []
        tmp = []

        def dfs(full):
            # 다 털었으면
            if not full:
                results.append(tmp[:])

            # recursion
            for n in full:
                next_arr = full[:] 
                next_arr.remove(n) # 중목 원소 없을 때만 가능

                tmp.append(n)
                dfs(next_arr)
                tmp.pop() # dfs 완전탐색 할 때는 다음 차례를 위해서 값 돌려놓기

        dfs(nums)
        return results