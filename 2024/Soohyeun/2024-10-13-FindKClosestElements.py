class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Base case
        if len(arr) == k:
            return arr

        # Binary search to find the left bound of the closest elements
        left, right = 0, len(arr) - k

        while left < right:
            mid = (left + right) // 2
            # Compare the distance between x and arr[mid] vs arr[mid + k]
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        # Slice the k closest elements
        return arr[left:left + k]

        # Time Complexity: O(logn)
        # Space Complexity: O(1)