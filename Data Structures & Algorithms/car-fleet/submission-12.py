class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True) #most ahead to most behind [7,4, 1, 0]

        fleets = 1
        prevTime = (target - pair[0][0]) / pair[0][1] #compute time of most ahead
        for i in range(1, len(pair)):
            currCar = pair[i] #prev's position is ahead of curr car's position
            currTime = (target - currCar[0]) / currCar[1]
            if currTime > prevTime: #if time of position behind > time of position ahead -> it can't catch up
                fleets += 1
                prevTime = currTime #see if this new fleet has more cars in it
        return fleets