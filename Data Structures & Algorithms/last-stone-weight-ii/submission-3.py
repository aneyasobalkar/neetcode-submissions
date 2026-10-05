class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {}
        total = sum(stones)
        #each call returns the smallest absolute difference between two piles
        def dfs(i, sum_so_far):
            if i >= len(stones):
                dp[(i, sum_so_far)] = abs((total - sum_so_far) - sum_so_far)
                return dp[(i, sum_so_far)]
            if (i, sum_so_far) in dp:
                return dp[(i, sum_so_far)]
            no_smash = dfs(i+1, sum_so_far)
            smash = dfs(i+1,  sum_so_far + stones[i])
            dp[(i, sum_so_far)] = min(no_smash, smash)
            return dp[(i, sum_so_far)]
        dfs(0, 0)
        return dp[(0,0)]