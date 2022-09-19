# 🥲 time out solution 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result_dict = [0] * len(nums)
        for i, num in enumerate(nums):
            # 현재요소를 제외한 배열
            except_arr = nums[:i] + nums[i+1:]
            
            # 현재요소 제외한 모든값을 곱해서 결과배열에 저장
            result_dict[i] = reduce(lambda x, y: x * y, except_arr)
        return result_dict
