class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []

        # 要帶入什麼參數
        def backtrace(start):
            # 收集條件是什麼
            res.append(path[:])

            # for loop range 為何
            for i in range(start, len(nums)):
                # i > start 確保不是該層第一個值
                # nums[i-1] == nums[i] 與該層前一個值相同
                # 同時滿足以上兩個條件，會導致一樣的組合出現
                if i > start and nums[i-1] == nums[i]:
                    continue
                # 帶入路徑，有無條件?
                path.append(nums[i])
                # dfs
                backtrace(i+1)
                # 撤銷路徑
                path.pop()
                
        backtrace(0)
        return res