class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        max_area = 0
        stack = []

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                node = stack.pop()
                l = -1 if not stack else stack[-1]
                r = i
                max_area = max(max_area, (r-l-1)*heights[node])
            stack.append(i)
        return max_area