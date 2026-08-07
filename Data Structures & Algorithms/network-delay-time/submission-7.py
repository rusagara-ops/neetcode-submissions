

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
      

        adjacency = defaultdict(list)

        for u,v,t in times:
            adjacency[u].append((v,t))

        distances = {}
        for node in range(1,n+1):
            distances[node] = float("inf")

        stack = [(k,0)]

        def dfs():
            while stack:
                node,time = stack.pop()
                if distances[node] <= time:
                    continue
                distances[node] = time

                for dest, t in adjacency[node]:
                    stack.append((dest,t + time))

        dfs()

        result = max(distances.values())

        if result < float("inf"): return result
        else: return -1

    # if result < float("inf")


