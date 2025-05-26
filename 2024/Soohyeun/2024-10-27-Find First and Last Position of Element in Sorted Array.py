class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        first_index = -1
        last_index = -1
        # mode 0: initial (check left, right), 1: check only left, 2: check only right
        def find_target(left, right, mode):
            nonlocal first_index
            nonlocal last_index
            curr_left = left
            curr_right = right
            mid = (curr_left + curr_right) // 2
            while curr_left <= curr_right:
                mid = (curr_left + curr_right) // 2
                if nums[mid] == target:
                    if mode == 0 or mode == 1:
                        first_index = mid
                        if mid - 1 >= 0 and nums[mid - 1] == target:
                            find_target(left, mid - 1, 1)
                    if mode == 0 or mode == 2:
                        last_index = mid
                        if mid + 1 < len(nums) and nums[mid + 1] == target:
                            find_target(mid + 1, right, 2)
                    break
                elif nums[mid] < target:
                    curr_left = mid + 1
                else:
                    curr_right = mid - 1

        find_target(0, len(nums) - 1, 0)

        return [first_index, last_index]