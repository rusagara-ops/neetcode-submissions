class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        current = []
        total = 0

        def dfs(start, total):
            if total == target:
                result.append(current.copy())
                return
            if total > target:
                return

            for i in range(start, len(nums)):
                
                current.append(nums[i])
                dfs(i, total + nums[i])
                current.pop()

                

        dfs(0, 0)
        return result

