class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        ans = [intervals[0]]

        for i in intervals:
            prev = ans[-1]
            if prev[1] >= i[0]:
                ans[-1] = [prev[0], max(prev[1], i[1])]
            else:
                ans.append(i)
        return ans
