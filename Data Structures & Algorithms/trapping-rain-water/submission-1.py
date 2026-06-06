class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        l = 0
        r = len(height) -1
        l_max, r_max = height[l], height[r]

        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                total += (l_max - height[l])
            else:
                r -= 1
                r_max = max(r_max, height[r])
                total += (r_max - height[r])
        return total