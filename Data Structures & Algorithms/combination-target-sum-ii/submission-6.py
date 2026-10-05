class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, curr_arr, curr_sum):
            if curr_sum == target:
                res.append(list(curr_arr))
                return
            if curr_sum > target or i == len(candidates):
                return
            curr_arr.append(candidates[i])
            dfs(i+1, curr_arr, curr_sum + candidates[i])
            curr_arr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, curr_arr, curr_sum)
        dfs(0, [], 0)
        return res