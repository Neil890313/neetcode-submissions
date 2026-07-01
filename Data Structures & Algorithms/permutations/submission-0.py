class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)

        def backtrace():
            # 收集條件
            if len(path) == len(nums): 
                res.append(path[:])
                return
            # for loop 這一行的參數的判斷依據是順序
            # 這一題順序不同是不同答案(與前幾題不同)
            for i in range(len(nums)):
                # 加入路徑
                # 如果被用過則跳過
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                # dfs
                backtrace()
                # 撤銷路徑
                path.pop()
                used[i] = False
            
        backtrace()
        return res

