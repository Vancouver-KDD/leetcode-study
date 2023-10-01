class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ### method 1
        # arr.sort(key=lambda i:abs(i-x))
        # return sorted(arr[:k])

        # ### method 2 (heap)
        # arr.sort(key=lambda i:abs(i-x))
        # heap = []
        # for i in range(k):
        #     heapq.heappush(heap, arr[i])
        # return sorted(heap)
    
        ### method 3 (binary search)
        # find the closest element to x
        # find the left and right bound
        # return the elements between the left and right bound
        left, right = 0, len(arr)-1
        while left < right:
            mid = (left+right)//2
            if arr[mid] < x:
                left = mid+1
            else:
                right = mid

        if left == 0:
            return arr[:k]
        elif left == len(arr)-1:
            return arr[-k:]
        else:
            if abs(arr[left-1]-x) <= abs(arr[right+1]-x):
                return arr[left-k:left]
            else:
                return arr[right+1:right+k+1]