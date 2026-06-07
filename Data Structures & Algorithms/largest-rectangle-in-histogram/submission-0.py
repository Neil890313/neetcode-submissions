class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area_list = [1]*len(heights)
        

        for idx, num in enumerate(heights):
            while stack and heights[stack[-1]] >= num:
                h_index = stack.pop()
                left_boundry = -1 if not stack else stack[-1]
                area_list[h_index] = heights[h_index] * (idx - left_boundry - 1)
            stack.append(idx)
        
        while stack:
            h_index = stack.pop()
            left_boundry = -1 if not stack else stack[-1]
            area_list[h_index] = heights[h_index] * (len(heights) - left_boundry -1)
        

        return max(area_list)