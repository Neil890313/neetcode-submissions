class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 分組，使得左邊的組的人數 == 總人數/2
        # 對短的切
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        # Numbers that need
        m = len(nums1)
        n = len(nums2)
        half = (m + n + 1)//2

        # 針對nums1切割，所以 l 為 nums1 的開頭， r 為 nums1 的結尾
        l, r = 0, m
        # 分組
        while l <= r:
            # Guess the number of left group using mid
            left_number = (l+r)//2
            right_number = half - left_number

            # Boundary
            # nums1 切割線的左一個元素
            l1 = float("-inf") if left_number == 0 else nums1[left_number-1]
            # nums1 切割線的右一個元素
            r1 = float('inf') if left_number == m else nums1[left_number]
            # nums2 切割線的左一個元素
            l2 = float("-inf") if right_number == 0 else nums2[right_number-1]
            # nums2 切割線的右一個元素
            r2 = float('inf') if right_number == n else nums2[right_number]

            # 判斷切割的成不成功
            if l1 <= r2 and l2 <= r1:
                if (m+n)%2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2))/2.0
            elif l1 > r2:
                r = left_number-1
            else:
                l = left_number + 1