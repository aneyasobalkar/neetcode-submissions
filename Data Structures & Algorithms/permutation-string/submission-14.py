class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        
        index = 0
        while index < len(s2):
            s2_sub = sorted(s2[index:index + len(s1)])
#            s2_sub.sort()
            if s1 == s2_sub:
                return True
            index += 1        
        return False

                