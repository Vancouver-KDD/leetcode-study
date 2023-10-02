class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=int(a,2)
        b=int(b,2)
        c=a+b
        c=bin(c)
        return c[2:]