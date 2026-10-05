from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        l, r = 0, len(s1)-1
        s1_map = Counter(s1)
        while r < len(s2):
            if Counter(s2[l:r+1]) == s1_map:
                return True
            else:
                l += 1
                r+=1
        return False
