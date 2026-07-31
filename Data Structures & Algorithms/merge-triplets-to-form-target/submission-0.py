class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        hashmap = {0: set(),
        1: set(),
        2: set()}

        for triplet in triplets:
            hashmap[0].add(triplet[0])
            hashmap[1].add(triplet[1])
            hashmap[2].add(triplet[2])

        for i in range(len(target)):
            if target[i] != sorted(hashmap[i])[-1]:
                return False

        return True