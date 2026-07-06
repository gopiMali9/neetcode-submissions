class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        left = 0
        right = k
        output = []
        while right <= len(nums):
            output.append(max(nums[left:right]))
            left += 1
            right +=1
        return output