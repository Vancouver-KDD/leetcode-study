class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def bit_counter(n):
            s = bin(n)[2:]
            temp = 0
            for i in s:
                if i == '1':
                    temp += 1
            return temp
        
        result = []
        
        for h in range(12):
            for m in range(60):
                if bit_counter(h) + bit_counter(m) == turnedOn:
                    result.append(f'{h}:{m:02}')
                    
        return result