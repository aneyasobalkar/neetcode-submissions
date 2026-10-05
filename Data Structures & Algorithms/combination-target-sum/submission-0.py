class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, curr_arr, total):
            if total > target or i >= len(nums):
                return
            if total == target:
                res.append(curr_arr)
                return
            curr_arr.append(nums[i])
            dfs(i, list(curr_arr), total + nums[i])
            curr_arr.pop()
            dfs(i+1, list(curr_arr), total)
        dfs(0, [], 0)
        return res