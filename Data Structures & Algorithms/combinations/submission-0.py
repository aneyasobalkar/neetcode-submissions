class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [num for num in range(1, n+1)]
        res = []
        def dfs(i, curr_arr, curr_size):
            if curr_size == k:
                res.append(list(curr_arr))
                return
            if i >= len(nums):
                return
            curr_arr.append(nums[i])
            dfs(i+1, curr_arr, curr_size + 1)
            curr_arr.pop()
            dfs(i+1, curr_arr, curr_size)
        dfs(0, [], 0)
        return res