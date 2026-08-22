class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        left, right = 0, n-1

        while left<right:
            area = (right-left)* min(heights[left], heights[right])

            max_area = max(max_area, area)

            if heights[right]>heights[left]:
                left+=1
            else:
                right-=1
        
        return max_area
        