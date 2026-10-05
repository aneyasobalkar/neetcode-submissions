class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_to_time = {position[i]: (target - position[i])/speed[i] for i in range(len(position))}
        position.sort(reverse = True)
        stack = [position[0]]
        for p in position[1:]:
            if (position_to_time[p] > position_to_time[stack[-1]]):
                stack.append(p)
        return len(stack)