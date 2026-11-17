class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1

        area = 0
        local_area = 0
        while left<right:
            local_area = (right-left) * min(heights[left], heights[right])
            area = max(local_area,area)
            
            if heights[left]<heights[right]:
                left+=1
            elif heights[right]<heights[left]:
                right-=1
            else:
                left+=1
                right-=1
        return area