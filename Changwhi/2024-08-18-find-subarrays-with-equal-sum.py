class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        dict1={}
        for i in range(len(nums)-1):
            x=sum(nums[i:i+2])
            dict1[i]=x
        list1=list(dict1.values())
        for i in range(len(list1)):
            j=i+1
            while j<len(list1):
                if list1[i]==list1[j]:
                    return True
                j+=1
        return False