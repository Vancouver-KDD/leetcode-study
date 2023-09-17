class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        permList = []
        perm = set(permutations(nums,len(nums)))
        
        for x in list(perm):
            permList.append(x)
        return permList