class Solution(object):
    def isHappy(self, n):
        s = set()
        while n != 1:
            if n in s: return False
            s.add(n)
            n = sum([int(i) ** 2 for i in str(n)]) # 1
        
        return True

# 1. By converting it to a string, you can iterate over each digit
#    List comprehension. The result is a list of the squared digits