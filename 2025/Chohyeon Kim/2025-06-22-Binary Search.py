class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #    0 1 2 3 4 5
        # [-1,0,3,5,9,12]
        #  l      l    r

        # 3 + 5 = 8 // 2 == 4

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            print(f"{left} {right} {mid}")

            

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1

            else:
                print(f"nums[mid] less than target")
                right = mid - 1

        return -1
        