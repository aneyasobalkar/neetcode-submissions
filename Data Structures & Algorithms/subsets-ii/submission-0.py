class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, curr_list):
            if i >= len(nums):
                if curr_list not in res:
                    res.append(list(curr_list))
                return
            curr_list.append(nums[i])
            dfs(i+1, list(curr_list))
            curr_list.pop()
            dfs(i+1, list(curr_list))
        dfs(0, [])
        return res