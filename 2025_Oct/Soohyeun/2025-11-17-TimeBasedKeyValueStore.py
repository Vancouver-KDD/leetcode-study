class TimeMap:

    def __init__(self):
        self.key_timestamps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_timestamps[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_timestamps:
            return ""
        stamps_values = self.key_timestamps[key]
        left, right = 0, len(stamps_values) - 1
        res = ""
        while left <= right:
            mid = (left + right) // 2
            if stamps_values[mid][0] <= timestamp:
                res = stamps_values[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)