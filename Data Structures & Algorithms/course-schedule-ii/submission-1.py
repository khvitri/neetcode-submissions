class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {crs : [] for crs in range(numCourses)}
        for crs, preReq in prerequisites:
            preMap[crs].append(preReq)

        res = []
        visiting, valid = set(), set()

        def dfs(crs):
            if crs in visiting:
                return False
            
            if crs in valid:
                return True
            
            visiting.add(crs)
            for preReq in preMap[crs]:
                if not dfs(preReq):
                    return False
            visiting.remove(crs)
            valid.add(crs)
            res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return res

