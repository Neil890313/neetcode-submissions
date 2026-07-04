class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            prev = ans[-1]
            now = intervals[i]  

            if prev[1] >= now[0]:
                ans[-1][0] = min(prev[0], now[0])
                ans[-1][1] = max(prev[1], now[1])
            else:
                ans.append(now)
        return ans
