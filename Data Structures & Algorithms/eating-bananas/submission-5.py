class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        maxK = max(piles)
        minK = 0
        k = maxK // 2
        def hours_with_k(k):
            curr_hours = 0
            for bananas in piles:
                if bananas > k:
                    time = math.ceil(bananas / k)
                    curr_hours += time
                else:
                    curr_hours += 1
            return curr_hours

        while k> minK and k < maxK:
            timeK = hours_with_k(k)
            if timeK > h:
                minK = k
                #k = ((maxK - minK)//2) + minK
            else:
                maxK = k
            k = (maxK  + minK)//2
        return maxK

            