class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        #Use hashset of indirect prerequisites
        #each course should point to an indirect prerequisite
        #Create this using DFS
        #Then just check if crs in pre when iterating through queries
        adjlist = {i:[] for i in range(numCourses)}
        for pre, crs in prerequisites:
            adjlist[crs].append(pre)


        def dfs(crs):
            if crs not in prereq_map:
                prereq_map[crs] = set([crs])
                for pre in adjlist[crs]:
                    prereq_map[crs] |= dfs(pre)
            return prereq_map[crs]


        prereq_map = {}
        for crs in range(numCourses):
            dfs(crs)
        res = []
        for pre, crs in queries:
            res.append(pre in prereq_map[crs])
        return res

