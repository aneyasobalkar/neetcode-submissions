class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        globalMax = (right - left) * min(heights[left], heights[right])
        while left < right:
            area =  (right - left) * min(heights[left], heights[right])
            globalMax = max(globalMax, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1
            
        return globalMax
