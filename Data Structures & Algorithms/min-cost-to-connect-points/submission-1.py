class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # set to store the visited ones
        # minheap to give us the shortest node's distance from the frontier
        # cost variable to keep track

        adjacency = defaultdict(list)  # gonna be adding (distance, destination)
        
        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i+1, len(points)):
                x2,y2 = points[j]

                dist = abs(x1-x2) + abs(y1-y2)

                adjacency[i].append((dist,j))
                adjacency[j].append((dist,i))

        # prims algortihm

        result = 0
        visited = set()
        minheap = [[0,0]] #(cost,node)

        while len(visited) < len(points):
            cost,node = heapq.heappop(minheap)
            if node in visited:
                continue
            visited.add(node)
            result += cost

            for distance, neighbor in adjacency[node]:
                if neighbor in visited:
                    continue
                heapq.heappush(minheap, (distance,neighbor))

        return result
