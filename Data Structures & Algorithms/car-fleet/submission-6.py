class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined_arr = [[position[i], speed[i]] for i in range(len(position))]
        combined_arr = sorted(combined_arr, key = lambda x: -x[0])
        times = [(target-item[0])/item[1] for item in combined_arr]
        stack = [times[0]]
        for time in times[1:]:
            if stack and time > stack[-1]:
                stack.append(time)
        return len(stack)

