class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        res_index = 0
        total = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            if total < 0:
                total = 0
                res_index = i + 1
        return res_index