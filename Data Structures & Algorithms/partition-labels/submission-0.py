class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        hashmap = {}

        for i in range(len(s)):
            hashmap[s[i]] = i

        result = []
        size = 0
        end = 0

        for i in range(len(s)):
            size += 1
            end = max(end, hashmap[s[i]])

            if i == end:
                result.append(size)
                size = 0

        return result




