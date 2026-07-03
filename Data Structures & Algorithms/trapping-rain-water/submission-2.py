class Solution:
    def trap(self, height: List[int]) -> int:

        total = 0

        for i in range(len(height)):

            left_max = height[:i]
            right_max = height[i+1:]

            if len(left_max) != 0 and len(right_max) != 0:

                if max(left_max) <= height[i] or height[i] >= max(right_max):
                    pass
                else:
                    min_wall = min(max(left_max),max(right_max))
                    curr_water = min_wall - height[i]
                    total += curr_water  
        
        return total