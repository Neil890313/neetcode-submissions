class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])

        ans = []
        inserted = False
        for i in intervals:
            if i[1] < newInterval[0]:
                ans.append(i)
            elif i[0] > newInterval[1]:
                if not inserted:
                    ans.append(newInterval)
                    inserted = True
                ans.append(i)
            else:
                newInterval = [
                    min(newInterval[0], i[0]),
                    max(newInterval[1], i[1])
                ]
        if not inserted:
            ans.append(newInterval)
        return ans

