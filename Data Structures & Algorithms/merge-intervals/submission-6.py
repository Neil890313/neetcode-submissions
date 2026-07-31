class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])

        ans = []
        ans.append(intervals[0])

        for i in intervals[1:]:
            prev = ans[-1]

            if i[0] <= prev[1]:
                ans[-1] = [min(i[0], prev[0]), max(i[1], prev[1])]
            else:
                ans.append(i)
        return ans
