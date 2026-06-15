class Solution:
    def numDecodings(self, s: str) -> int:
        #base case: if length of string is 0 there is one way to decode
        dp = {len(s):1}
        def dfs(i):
            #if we have cached this call already
            if i in dp:
                return dp[i]
            #if the next group starts with 0 return 0
            if s[i] == "0":
                return 0
            #must start with 1 then 
            res = dfs(i+1)
            #consider skipping two digits
            if i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "01233456")):
                res += dfs(i+2)
            dp[i] = res #dfs(i+1) + dfs(i+2)
            return res
        return dfs(0)


