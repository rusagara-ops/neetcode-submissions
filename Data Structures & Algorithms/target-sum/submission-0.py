class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def backtrack(i, currsum):

            if i == len(nums):
                if currsum == target:
                    return 1
                else:
                    return 0
            return backtrack(i+1, currsum + nums[i]) + backtrack(i+1, currsum - nums[i])


        return backtrack(0,0)
            