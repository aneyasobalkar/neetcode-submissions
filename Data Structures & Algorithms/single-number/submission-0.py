class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for num in nums:
            x = x ^ num
        return x
       #3 - 11
       #2 - 10
       #3 XOR 2 -> 01 -> 01
       #01 XOR 11 -> 10 -> 2

       #7 -> 0111
       #6 -> 0110
       #8 -> 1000

       # 7 XOR 6 -> 0001
       # 0001 (7 XOR 6 ) XOR 0110 -> 0111
       #0111 XOR 0111 -> 0000
       # 0000 XOR 1000 -> 1000
