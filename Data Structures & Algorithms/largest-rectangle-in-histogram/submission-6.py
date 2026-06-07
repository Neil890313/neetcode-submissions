class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #
        heights.append(0)
        # stack 中保存idx，並且從小排到大
        stack = []
        # 最大面積
        max_area = 0

        for idx, num in enumerate(heights):
            # monotonic 起手式
            # 因為後者如果比較小，則比較大的前者永遠不可能成為 heights
            # 注意，因為 stack 中存放的是 index
            while stack and heights[stack[-1]] >= num:
                h_index = stack.pop()
                # length 的左邊界是stack 前一項的 index，如果stack 空則為-1
                left_boundry = -1 if not stack else stack[-1]
                # length 的右邊界是目前值的 index
                current_area = heights[h_index] * (idx - left_boundry - 1)
                max_area = max(max_area, current_area)
            stack.append(idx)    

        return max_area