class TimeMap:

    def __init__(self):
        self.key_timestamps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_timestamps[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.key_timestamps:
            return ""

        timestamp_values = self.key_timestamps[key]
        left = 0
        right = len(timestamp_values)
        while left < right:
            middle = (left + right) // 2
            if timestamp_values[middle][0] <= timestamp:
                left = middle + 1
            else:
                right = middle

        return "" if right == 0 else timestamp_values[right - 1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)