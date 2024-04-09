"""
https://leetcode.com/problems/course-schedule/description/
"""

def canFinish(numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = { i:[] for i in range(numCourses)}
        
        for i, j in prerequisites:
            graph[i].append(j)

        visiting = set()
        visited = set()
        def dfs(start):
            if start in visiting:
                return True
            if start in visited:
                return False
            
            visiting.add(start)

            for el in graph[start]:
                if dfs(el):
                    return True
            visiting.remove(start)
            visited.add(start)
            return False

        for i in range(numCourses):
            if dfs(i):
                return False
        return len(visited) == numCourses