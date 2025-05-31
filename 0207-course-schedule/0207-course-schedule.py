class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        pmap = {i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            pmap[i].append(j)
        def dfs(crs):
            if crs in visit:
                return False
            if pmap[crs]==[]:
                return True
            
            visit.add(crs)
            for pre in pmap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            pmap[crs]= []
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True