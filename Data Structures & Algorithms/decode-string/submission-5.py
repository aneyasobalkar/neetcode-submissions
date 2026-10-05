class Solution:
    def decodeString(self, s: str) -> str:
        string_stack = []
        count_stack = []
        cur = "" #current stirng im building
        k = 0 #current multiplier im finding
        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            #store whatever has appeared before [ and our k value
            elif c == "[":
                string_stack.append(cur)
                count_stack.append(k)
                #reset to store information in brackets
                cur = ""
                k = 0
            #end of bracket
            elif c == "]":
                #temp =
                cur = string_stack.pop() +  cur * count_stack.pop() 
            else:
                cur += c
        return cur