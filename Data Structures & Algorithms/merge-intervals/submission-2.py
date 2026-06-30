class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals)
        if not sorted_intervals:
            return []
        ans = [sorted_intervals[0]]

        for i in range(1, len(sorted_intervals)):
            prev = ans[-1]
            if prev[1] >= sorted_intervals[i][0]:
                ans[-1] = [prev[0], max(prev[1], sorted_intervals[i][1])]
            else:
                ans.append(sorted_intervals[i])
        return ans