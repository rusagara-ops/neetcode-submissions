class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = Counter(tasks)

        maxheap = []
        for value in hashmap.values():
            maxheap.append(-value)

        heapq.heapify(maxheap)

        time = 0
        queue = deque()

        while maxheap or queue:
            time += 1
            if maxheap:
                currentcount = 1 + heapq.heappop(maxheap)
                if currentcount:
                    queue.append([currentcount, time + n])

            if queue and queue[0][1] == time:
                heapq.heappush(maxheap, queue.popleft()[0])
        
        return time



