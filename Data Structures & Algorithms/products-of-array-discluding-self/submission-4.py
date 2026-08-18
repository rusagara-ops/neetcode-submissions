class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        output = [1] * len(nums)
        for i in range(len(nums)):
            product *= nums[i]

        for j in range(len(nums)):
            if nums[j] == 0:
                output[j] = 0
            else:
                output[j] = product//nums[j]

        return output

        


