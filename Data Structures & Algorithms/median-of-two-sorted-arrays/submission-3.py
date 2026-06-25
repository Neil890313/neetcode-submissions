class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 分組
        if nums1 > nums2:
            nums1, nums2 = nums2, nums1
        # setting
        m, n = len(nums1), len(nums2)
        half = (m+n+1)//2
        l, r = 0, m

        while l <= r:
            left_team = (l+r)//2
            right_team = half-left_team

            # boundary
            l1 = float('-inf') if left_team == 0 else nums1[left_team-1]
            r1 = float('inf') if left_team >= m else nums1[left_team]
            l2 = float('-inf') if right_team == 0 else nums2[right_team-1]
            r2 = float('inf') if right_team >= n else nums2[right_team]

            if l1 <= r2 and l2 <= r1:
                if (m+n)%2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2))/2.0
            elif l1 > r2:
                r = left_team-1
            else:
                l = left_team+1