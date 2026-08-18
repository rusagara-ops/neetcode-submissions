class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        heap = []

        for key,value in hashmap.items():
            heapq.heappush(heap, (-value,key))
        

        for _ in range(k):
            val, key = heapq.heappop(heap)
            result.append(key)

        return result

        