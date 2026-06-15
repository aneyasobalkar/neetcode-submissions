class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_perm = {}
        for char in s1:
            s1_perm[char] = s1_perm.get(char, 0) + 1
        
        index = 0
        while index < len(s2):
            s2_sub = s2[index:index + len(s1)]
            s2_perm = {}
            for char in s2_sub:
                s2_perm[char] = s2_perm.get(char, 0) + 1
            if s1_perm == s2_perm:
                return True
            index += 1        
        return s1_perm == s2_perm

                