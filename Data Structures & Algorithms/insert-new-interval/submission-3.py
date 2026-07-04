class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        intervals.sort(key = lambda x:x[0])

        inserted = False
        for interval in intervals:
            # 不重疊，且比 newInterval 小，直接加入
            if not inserted:
                if interval[1] < newInterval[0]:
                    ans.append(interval)
                # 不重疊，且比 newInterval 小，先加入 newInterval 再加入 interval
                elif interval[0] > newInterval[1]:
                    ans.append(newInterval)
                    inserted = True
                    ans.append(interval)
                else:
                    newInterval[0] = min(newInterval[0], interval[0])
                    newInterval[1] = max(newInterval[1], interval[1])
            else:
                ans.append(interval)
                
        if not inserted:
            ans.append(newInterval)
        return ans


