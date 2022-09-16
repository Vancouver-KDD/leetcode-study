# hash map
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # new_dict[값] = 인덱스값 으로 딕셔너리를 만든다
        # 요소를 순회하며 target - 현재요소값이 있는지 확인하고,
        # 없다면 key, value로 저장하고
        # 있다면 각각 인덱스값을 반환한다
    
        num_dict = {}
        for i, num in enumerate(nums):
            if target - num in num_dict:
                return [i, num_dict[target - num]]
            num_dict[num] = i      


# two pointer
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # index를 반환해야 하기 때문에 튜플로 만들어 값을 유지한다 
        nums = enumerate(nums)

        # 투포인터를 사용하려면 정렬되어있어야 한다
        # value기준으로 정렬한다
        # python의 sort()는 팀소트로 O(n logn)이다
        
        nums = sorted(nums, key=lambda x: x[1])

        left, right = 0, len(nums) - 1

        while not left == right:
            if nums[left][1] + nums[right][1] < target:
                left += 1
            elif nums[left][1] + nums[right][1] > target:
                right -= 1
            else:
                return [nums[left][0], nums[right][0]]