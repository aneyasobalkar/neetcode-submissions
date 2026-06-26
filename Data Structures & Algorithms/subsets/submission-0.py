class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        if len(nums) == 0:
            return res
        else:
            sub = self.subsets(nums[1:])
            for subset in sub:
                res.append(subset)
                res.append([nums[0]] + subset)
        reset = set()
        for pair in res:
            reset.add(tuple(pair))
        res2 = []
        for tup in reset:
            res2.append(list(tup))
        return res2             
