class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []

        for i in range(len(nums)):
            product = 1
            temp = nums[:i]+nums[i+1:]
            for j in temp:
                product *= j
            output.append(product)

        return output
        