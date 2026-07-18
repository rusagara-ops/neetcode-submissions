from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        prereqsdict = {}

        indegree = [0] * numCourses

        for course in range(numCourses):
            prereqsdict[course] = []

        for course, prereq in prerequisites:
            prereqsdict[prereq].append(course)
            indegree[course] += 1
        
        queue = deque()

        for course in range(len(indegree)):
            if indegree[course] == 0:
                queue.append(course)

        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in prereqsdict[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) != numCourses:
            return []
        print(result)
        return result



