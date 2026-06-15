class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined_arr = [[position[i], speed[i]] for i in range(len(position))]
        combined_arr = sorted(combined_arr, key = lambda x: -x[0])
        stack = []
        for item in combined_arr:
            time = (target-item[0])/item[1]
            if not stack:
                stack.append(time)
            elif stack and time > stack[-1]:
                stack.append(time)
        return len(stack)

