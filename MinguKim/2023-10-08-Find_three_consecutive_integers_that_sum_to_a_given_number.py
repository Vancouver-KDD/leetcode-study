class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        return sorted([num//3-1,num//3,num//3+1]) if num%3==0 else []