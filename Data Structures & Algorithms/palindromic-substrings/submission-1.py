class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalindrome(s):
            l = 0
            r = len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        dp = [0 for i in range(len(s))]
        for index in range(len(s)):
            for start in range(0, index+1):
                #print(s[start:index])
                #print(isPalindrome(s[start:index+1]))
                if isPalindrome(s[start:index+1]):
                    dp[index] += 1
        #print(dp)
        return sum(dp)