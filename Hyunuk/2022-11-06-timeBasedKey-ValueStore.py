import collections

class TimeMap:

    def __init__(self):
        self.hm = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hm:
            return ""
        return self._helper(self.hm[key], timestamp)
    
    def _helper(self, arr, time):
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m][1] == time:
                return arr[m][0]
            elif arr[m][1] < time:
                l = m + 1
            else:
                r = m - 1
        return arr[l-1][0] if l > 0 else ""
                

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
"""
[1, 4, 6]
5

"""
