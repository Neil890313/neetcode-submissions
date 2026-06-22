class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # step1: find a meet point on the cycle
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # step2: the distance from head to entrance is equal to the distance from meet point to entrance
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow