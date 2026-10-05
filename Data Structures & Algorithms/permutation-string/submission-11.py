class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        l, r = 0, len(s1)-1
        s1= "".join(sorted(s1))
        while r < len(s2):
            if "".join(sorted(s2[l:r+1])) == s1:
                return True
            else:
                l += 1
                r+=1
        return False
