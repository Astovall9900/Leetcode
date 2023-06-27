class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        visit = set()
        def dfs(course):
            if course in visit:
                return False
            if adj[course] == []:
                return True
            visit.add(course)
            for dep in adj[course]:
                if not dfs(dep): return False
            visit.remove(course)
            adj[course] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
