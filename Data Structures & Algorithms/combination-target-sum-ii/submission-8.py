class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, curr_arr, curr_sum):
            if curr_sum == target and curr_arr not in res:
                res.append(curr_arr)
                return
            if i >= len(candidates) or curr_sum > target:
                return
            dfs(i+1, curr_arr + [candidates[i]], curr_sum + candidates[i])
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, curr_arr, curr_sum)
        dfs(0, [], 0)
        return res