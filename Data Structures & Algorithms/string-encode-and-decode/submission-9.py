class Solution:

    def encode(self, strs: List[str]) -> str:
        comprised_str = ""
        for string in strs:
            comprised_str += (str(len(string)) + "#")
            comprised_str += string
        return comprised_str
    def decode(self, s: str) -> List[str]:
        index = 0
        list_str = []
        while index < len(s):
            j = index
            while s[j] != "#":
                j += 1
            size = int(s[index:j])
            index = j + 1
            j = index + size
            list_str.append(s[index:j])
            index = j
        return list_str