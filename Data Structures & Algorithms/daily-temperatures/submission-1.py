class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [(temperatures[0], 0)]
        for index, temp in enumerate(temperatures[1:], 1):
            if temp > stack[-1][0]:
                while stack and temp > stack[-1][0]:
                    last_val, last_index = stack.pop()
                    result[last_index] = index - last_index
            stack.append((temp, index))

        return result