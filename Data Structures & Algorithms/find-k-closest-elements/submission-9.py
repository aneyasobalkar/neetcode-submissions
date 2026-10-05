class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        for j in range(k):
            res.append(arr[j])
        for i in range(k, len(arr)):
            if (abs(arr[i] - x) < abs(res[0]-x)):
                res.pop(0)
                res.append(arr[i])
        return res