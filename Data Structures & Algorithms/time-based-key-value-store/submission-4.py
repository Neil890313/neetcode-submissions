class TimeMap:

    def __init__(self):
        self.check_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.check_dict[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        now_list = self.check_dict[key]
        l = 0
        r = len(now_list)-1
        ans = ''

        while l <= r:
            mid = (l+r)//2
            if now_list[mid][1] <= timestamp:
                ans = now_list[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return ans
