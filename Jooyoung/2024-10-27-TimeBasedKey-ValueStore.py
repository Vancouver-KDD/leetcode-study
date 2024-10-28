from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        val = ""
        l = 0
        r = len(values) - 1

        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                val = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return val

# Input:
# ["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]

# Output:
# [null, null, "happy", "happy", null, "sad"]

# Explanation:
# TimeMap timeMap = new TimeMap();
# timeMap.set("alice", "happy", 1);  // store the key "alice" and value "happy" along with timestamp = 1.
# timeMap.get("alice", 1);           // return "happy"
# timeMap.get("alice", 2);           // return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
# timeMap.set("alice", "sad", 3);    // store the key "alice" and value "sad" along with timestamp = 3.
# timeMap.get("alice", 3);           // return "sad"

# values = [["happy", 1], ["joyful", 2], ["sad", 5]]
# l = 0
# r = 2
# val = ""
# m = 1