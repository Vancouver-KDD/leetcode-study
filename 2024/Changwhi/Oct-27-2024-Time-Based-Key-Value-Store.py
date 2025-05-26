class TimeMap:
    """
    hash? 

        hash
        key : value 
    just key    [[value, time]] <- just list inside of list
                key value

        declare and initialize hash mpa

        set
            find value
                if key does not exist then create hash first
            and
            assgin that key value into hash.

        get
            find a value of key
            value is list

            you can use binary search on that list.
    """
    def __init__(self):
        self.storedData = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storedData:
            self.storedData[key] = []
        self.storedData[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        # you don't need to set up the result when the key does not exist in a hashmap
        targetList = self.storedData.get(key, [])
        
        left, right = 0, len(targetList) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if targetList[mid][1] <= timestamp:
                res = targetList[mid][0]
                left = mid + 1
            else:
                right = mid -1
        return res
                
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)