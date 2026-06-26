class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #Create graph
        adjList = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        path = []
        visited = set()
        marked = set()
        def dfs(crs):
            if crs in marked:
                return True
            if crs in visited:
                return False
            visited.add(crs)
            for pre in adjList[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            marked.add(crs)
            path.append(crs)
            return True
        
        for crs in range(numCourses):
            if crs not in marked:
                if not dfs(crs):
                    return []
        return path
