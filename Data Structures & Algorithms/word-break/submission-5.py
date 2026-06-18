class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Why I got this wrong? I didn't even get the recursive implementation correct.
        I also didn't know what to store on each recursive call. 
        """
        dp = [False for i in range(len(s) + 1)]
        dp[len(s)] = True
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if dp[i]:
                    break
                if i + len(word) <= len(s) and s[i: i+ len(word)] in wordDict:
                    dp[i] = dp[i + len(word)]
        return dp[0]
