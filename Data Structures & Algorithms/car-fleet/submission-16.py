class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)] #O(n) time
        pair.sort(reverse=True) # O(nlogn)

        fleets = len(pair)
        prevTime = (target - pair[0][0]) / pair[0][1]
        #O(n) time
        for i in range(1, len(pair)):
            currTime = (target - pair[i][0]) / pair[i][1]
            #if overlap
            if currTime <= prevTime:
                fleets -= 1 #keep prevTime the same bc thats the farthest ahead
            else:
                prevTime = currTime #now see if more fleets are in the same one as prevTime

        return fleets