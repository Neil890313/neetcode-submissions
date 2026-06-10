class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        node = self.store.get(key, '')
        if node:
            ans = ''
            for i in node:
                if i[1] <= timestamp:
                    ans = i[0]
            return ans
        else:
            return ''
