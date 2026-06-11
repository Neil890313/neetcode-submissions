class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 針對小的進行切割，因此首先要找出最短的
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # Setting
        m, n = len(nums1), len(nums2)

        # 針對較短的 nums1 進行切割
        l, r = 0, m
        half_num = (m+n+1)//2

        while l <= r:
            # 左右兩邊的組別大小
            # 左邊
            i = (l+r)//2
            # 右邊
            j = half_num-i

            # 兩個組各自切線的左右守衛，以及boundary
            l1 = float('-inf') if i == 0 else nums1[i-1]
            r1 = float('inf') if i == m else nums1[i]

            l2 = float('-inf') if j == 0 else nums2[j-1]
            r2 = float('inf') if j == n else nums2[j]

            # 判斷左右，以移動切割線
            # 完美切割
            if l1 <= r2 and l2 <= r1:
                # 如果總數為奇數
                if (m+n)%2 == 1:
                    return  max(l1, l2)
                else:
                    return (min(r1, r2) + max(l1, l2))/2.0
            elif l1 > r2:
                r = i - 1
            else:
                l = i + 1








