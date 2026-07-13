class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        notPreReqCrs = set([i for i in range(numCourses)])
        preMap = {crs : [] for crs in range(numCourses)}
        for crs, preReq in prerequisites:
            preMap[crs].append(preReq)
            if preReq in notPreReqCrs: notPreReqCrs.remove(preReq)

        if not notPreReqCrs: return []

        res = []
        valid = set()
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            
            if crs in valid:
                return True
            
            if preMap[crs] == []:
                valid.add(crs)
                res.append(crs)
                return True
            
            visiting.add(crs)
            for preReq in preMap[crs]:
                if not dfs(preReq):
                    return False
            
            visiting.remove(crs)
            valid.add(crs)
            res.append(crs)
            return True

        for crs in notPreReqCrs:
            if not dfs(crs):
                return []
        
        return res

