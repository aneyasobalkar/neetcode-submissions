class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(target - position[i])/speed[i] for i in range(len(position))]
        position_to_time = {position[i]: times[i] for i in range(len(position))}
        position.sort(reverse = True)
        stack = [position[0]]
        for p in position[1:]:
            #print(p, position_to_time[p])
            #print(stack[-1],position_to_time[stack[-1]])
            #print( f"{position_to_time[p] < position_to_time[stack[-1]]}")
            #if the position behind is faster than position behind -> add to stack
            if (position_to_time[p] > position_to_time[stack[-1]]):
                stack.append(p)
            # the car behind catches up to the car ahead. stores that further ahead car's position
        return len(stack)