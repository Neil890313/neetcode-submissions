class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        max_area = 0

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                node = stack.pop()
                height = heights[node]
                left = -1 if not stack else stack[-1]
                right = i
                now_area = (right-left-1)*height
                max_area = max(max_area, now_area)

            stack.append(i)

        return max_area