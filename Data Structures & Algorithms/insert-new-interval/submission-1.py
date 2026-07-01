class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        token = False
        for i in intervals:
            if i[1] >= newInterval[0] and i[0] < newInterval[1]:
                i[0] = min(i[0], newInterval[0])
                i[1] = max(i[1], newInterval[1])
                token = True
                break
        if not token:
            intervals.append(newInterval)
            intervals = sorted(intervals)      

        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            prev = ans[-1]
            if prev[1] >= intervals[i][0]:
                ans[-1][1] = max(prev[1], intervals[i][1])
            else:
                ans.append(intervals[i])
        return ans