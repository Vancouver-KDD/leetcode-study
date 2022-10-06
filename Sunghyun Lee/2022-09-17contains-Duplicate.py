class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mydict = dict()
        for i in nums:
            if(mydict.get(i) == None):
                mydict[i] = 1
            else:
                return True
        return False
