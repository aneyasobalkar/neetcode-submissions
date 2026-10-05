class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined_arr = [[position[i], speed[i]] for i in range(len(position))]
        #Sort in descending order such that its in order whos closest to target
        combined_arr.sort(reverse=True)
        """if the time of a further ahead position is greater than the position behind,
        they overlap, so that means they're in the same fleet. 
        Position and speed become the same.
        """ 
        times = [(target-item[0])/item[1] for item in combined_arr]
        #let's keep track of the fleets
        fleets = [times[0]]
        for time in times[1:]:
            #add a new fleet or keep in the same fleet
            """
            if the position is behind and it takes more time to get there.
            There is never overlap, so they cannot be in the same fleet.
            Thus, it is its own fleet.
            """
            if time > fleets[-1]:
                fleets.append(time)
        return len(fleets)

