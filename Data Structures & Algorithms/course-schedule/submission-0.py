class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adjList[crs].append(pre)

        visited = set()
        def dfs(i):
            if i in visited:
                return False
            if adjList[i] == []:
                return True
            visited.add(i)
            neighbors = adjList[i]
            for neighbor in neighbors:
                if not dfs(neighbor):
                    return False
            visited.remove(i)
            adjList[i] = []
            return True

        for crs in adjList.keys():
            if not dfs(crs):
                return False
        return True