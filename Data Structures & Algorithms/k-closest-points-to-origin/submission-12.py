class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        kPoints = [points[0]]
        maxKDist = (points[0][0]**2 + points[0][1]**2)**0.5
        for point in points[1:]:
            x, y = point
            dist = (x**2 + y**2)**0.5
            if dist < maxKDist and len(kPoints) == k:
                kPoints.sort(key = lambda pos:(pos[0]**2 + pos[1]**2)**0.5)
                kPoints.pop()
                if kPoints:
                    final_dist = (kPoints[-1][0]**2 + kPoints[-1][1]**2)**0.5
                    maxKDist = max(dist, final_dist)
                else:
                    maxKDist = dist
                kPoints.append(point)
            elif len(kPoints) < k:
                kPoints.append(point)
                maxKDist = max(dist, maxKDist)
        return kPoints