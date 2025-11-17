class TimeMap(object):
    def __init__(self):
        self.store = {}
        
    def set(self, key, value, timestamp):
        if not key in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if not key in self.store:
            return ""

        arr = self.store[key]
        if len(arr) == 0:
            return ""
        elif arr[0][0] > timestamp:
            return ""
        elif arr[-1][0] < timestamp:
            return arr[-1][1]

        i, j = 0, len(arr) - 1
        m = None
        while i <= j:
            m = int((i+j)/2)

            if timestamp == arr[m][0]:
                return arr[m][1]
            elif timestamp < arr[m][0]:
                j = m - 1
            else:
                i = m + 1

        if arr[m][0] > timestamp:
            return arr[m-1][1]
            
        return arr[m][1]