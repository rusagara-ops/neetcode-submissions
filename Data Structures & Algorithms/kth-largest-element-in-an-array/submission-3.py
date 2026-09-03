import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heap.append(-num)

        heapq.heapify(heap)
        
        result = []

        for _ in range(k):
            num = heapq.heappop(heap)
            result.append(-num)

        return result[-1]

        