class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        dp[0] = 1
        for i in range(1,len(nums)):
            #if consecutive
            traveler = i - 1
            max_len = 0
            #while not consecutive
            while traveler >= 0:
                if nums[i] > nums[traveler]:
                    max_len = max(max_len, dp[traveler])
                traveler -= 1
            dp[i] = max_len + 1
        return max(dp)