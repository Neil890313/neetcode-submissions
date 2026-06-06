class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        l = 0
        r = len(heights) -1

        while l < r:
            min_height = min(heights[l], heights[r])
            max_water = max(max_water, min_height*(r-l))

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_water