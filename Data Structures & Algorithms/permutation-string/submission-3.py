class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_perm = {}
        for char in s1:
            s1_perm[char] = s1_perm.get(char, 0) + 1
        k = len(s1)
        s2_sub = s2[:k]
        index = 1
        while index < len(s2):
            s2_perm = {}
            for char in s2_sub:
                s2_perm[char] = s2_perm.get(char, 0) + 1
            #print(s2_perm)
            if s1_perm == s2_perm:
                return True
            s2_sub = s2_sub[1:] + s2[index]
            #print(s2_sub)
            index += 1
        s2_perm = {}
        for char in s2_sub:
            s2_perm[char] = s2_perm.get(char, 0) + 1
        return s1_perm == s2_perm

                