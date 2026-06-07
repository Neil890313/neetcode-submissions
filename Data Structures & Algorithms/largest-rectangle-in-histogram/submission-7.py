class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 究級黑魔法：如果在最後放入0，則可以清除所有殘留在 stack 中的值，且更重要的是0 的 idx 為 len(heights)
        # 正式原本殘留在 stack 中的值的右邊界
        heights.append(0)
        # stack 中保存idx，並且從小排到大
        stack = []
        # 最大面積
        max_area = 0

        for idx, num in enumerate(heights):
            # monotonic 起手式
            # 因為後者如果比較小，則比較大的前者永遠不可能成為 heights
            # 注意，因為 stack 中存放的是 index，因此一定要 heights[stack[-1]]，錯很多次
            while stack and heights[stack[-1]] >= num:
                h_index = stack.pop()
                # length 的左邊界是stack 前一項的 index，如果stack 空則為-1
                left_boundry = -1 if not stack else stack[-1]
                # length 的右邊界是目前值的 index
                current_area = heights[h_index] * (idx - left_boundry - 1)
                max_area = max(max_area, current_area)
            stack.append(idx)    

        return max_area