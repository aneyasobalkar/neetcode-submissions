class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        for i,c in enumerate(s):
            hashmap[c] = i
        size = 0
        end = 0
        res = []
        for i, c in enumerate(s):
            end = max(hashmap[c], end)
            size += 1
            if i == end:
                res.append(size)
                size = 0



        return res