class TimeMap:

    def __init__(self):
        
        self.storage = {} # key:str, value: List[[int, str]] 

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.storage:
            self.storage[key] = []
        
        self.storage[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        
        res = ""
        
        if key not in self.storage:
            return res
        
        values = self.storage[key]
        
        l, r = 0, len(values)-1
        
        while l <= r:
            m = (l+r) //2
            
            if values[m][0] <= timestamp:
                res = values[m][1]
                l = m+1
            else:
                r = m-1
        
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)