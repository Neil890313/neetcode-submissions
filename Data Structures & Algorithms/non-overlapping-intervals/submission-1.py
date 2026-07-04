class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 排序(按 end)
        intervals.sort(key = lambda x:x[1])
        # 一個變數記錄「目前保留的最後結束時間」
        prev_end = intervals[0][1]
        # 一個計數器記錄「刪除了幾個」
        ans = 0
        # 掃過所有區間,判斷衝突與否,更新變數或計數器       
        for i in intervals[1:]:
            if prev_end > i[0]:
                prev_end = min(prev_end, i[1])
                ans += 1
            else:
                prev_end = i[1]
        return ans



