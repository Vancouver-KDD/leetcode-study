class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Step 1: Sort the numbers to make it easier to use two pointers
        nums.sort()
        # Step 2: Create a list to store all unique triplets
        answer = []

        # Step 3: Loop through each number as the first number in the triplet
        for x in range(len(nums)):
            # Skip duplicate numbers to avoid repeated triplets
            if x > 0 and nums[x] == nums[x - 1]:
                continue

            # Use two pointers: one starts just after x, and one at the end
            y = x + 1
            z = len(nums) - 1

            # Step 4: Move the two pointers to find pairs that sum with x to 0
            while y < z:
                total = nums[x] + nums[y] + nums[z]

                if total == 0:
                    # Found a triplet that sums to zero
                    answer.append([nums[x], nums[y], nums[z]])
                    # Move 'y' forward to find the next possible pair
                    y += 1

                    # Skip duplicate numbers for 'y' to avoid repeated triplets
                    while y < z and nums[y] == nums[y - 1]:
                        y += 1

                elif total > 0:
                    # If the sum is too big, move the right pointer left
                    z -= 1
                else:
                    # If the sum is too small, move the left pointer right
                    y += 1

        # Step 5: Return the list of all unique triplets
        return answer