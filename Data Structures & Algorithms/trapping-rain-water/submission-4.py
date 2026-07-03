class Solution:
    def trap(self, height: List[int]) -> int:

        total = 0

        for i in range(len(height)):

            left_max = height[:i]
            right_max = height[i+1:]


            if len(left_max) != 0 and len(right_max) != 0:
                l_maxi  = max(left_max)
                r_maxi = max(right_max)

                if l_maxi <= height[i] or height[i] >= r_maxi:
                    pass
                else:
                    min_wall = min(l_maxi,r_maxi)
                    curr_water = min_wall - height[i]
                    total += curr_water  
        
        return total