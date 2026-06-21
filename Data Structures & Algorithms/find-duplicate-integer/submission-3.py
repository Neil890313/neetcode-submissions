class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ## 排序
        # nums.sort()
        # prev = None

        # for i in nums:
        #     if i == prev:
        #         return i
        #     prev = i
        # 把陣列當成一條隱藏的 linked list,找重複數字就等於找環的入口點
        # step1: Find a meet point on the cycle
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # step2: The distance from head to entrance is equal to the distance from meet point on the cycle to entrance
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow