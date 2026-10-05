class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 0:
            return [[]]
        subperm = self.permute(nums[1:])
        for perm in subperm:
            for j in range(0, len(perm)+1):
                perm_copy = list(perm)
                perm_copy.insert(j, nums[0])
                res.append(perm_copy)
        return res