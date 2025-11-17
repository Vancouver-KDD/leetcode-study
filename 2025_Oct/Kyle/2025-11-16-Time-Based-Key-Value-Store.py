class TimeMap(object):
    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key, value, timestamp):
        self.time_map[key].append((value, timestamp))

    def get(self, key, timestamp):
        left = 0
        right = len(self.time_map[key]) - 1
        answer = ""

        while left <= right:
            mid = (left + right) // 2
            latest_timestamp = self.time_map[key][mid][1]

            if latest_timestamp <= timestamp:
                answer = self.time_map[key][mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return answer
