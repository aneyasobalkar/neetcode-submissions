class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        #[-4, -1,-1,0,1,2]
        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum == 0:
                    curr_tuple = tuple([nums[i], nums[j], nums[k]])
                    res.add(curr_tuple)
                if curr_sum > 0:
                    k -= 1
                else:
                    j += 1
        return list(res)