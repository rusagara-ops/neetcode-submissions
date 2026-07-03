class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        n = len(nums)
        count = 0

        while r < n-1:
            farthest = 0

            for i in range(l, r+1):
                farthest = max(i+nums[i], farthest)

            l = r
            r = farthest
            count += 1

        return count
