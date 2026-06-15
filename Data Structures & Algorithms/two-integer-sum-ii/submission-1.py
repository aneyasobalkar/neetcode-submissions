class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers) -1 
        while left < right:
            other_target = target - numbers[left]
            if other_target == numbers[right]:
                return [left+1, right+1]
            if other_target < numbers[right]:
                right -= 1
            else:
                left += 1
        