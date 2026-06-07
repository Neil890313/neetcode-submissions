class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        

        for idx, num in enumerate(heights):
            while stack and heights[stack[-1]] >= num:
                h_index = stack.pop()
                left_boundry = -1 if not stack else stack[-1]
                current_area = heights[h_index] * (idx - left_boundry - 1)
                max_area = max(max_area, current_area)
            stack.append(idx)
        
        while stack:
            h_index = stack.pop()
            left_boundry = -1 if not stack else stack[-1]
            current_area = heights[h_index] * (len(heights) - left_boundry - 1)
            max_area = max(max_area, current_area)
        

        return max_area