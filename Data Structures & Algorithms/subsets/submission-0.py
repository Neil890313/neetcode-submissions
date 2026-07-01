class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrace(start):
            res.append(path[:])
            # 透過設定 start:len(nums)，保證只能往後選，不能回頭選
            for i in range(start, len(nums)):
                # 增加新選項
                path.append(nums[i])
                # 向下探索
                backtrace(i+1)
                # 撤銷選項
                path.pop()
        backtrace(0)

        return res