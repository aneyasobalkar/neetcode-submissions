class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_k = r
        while l <= r:
            hours = 0
            k = (l+r)//2
            for bananas in piles:
                if bananas <= k:
                    hours += 1
                else:
                    hours += math.ceil(bananas / k)
            if hours <= h:
                min_k = k
                r = k - 1
            else:
                l = k + 1
        return min_k