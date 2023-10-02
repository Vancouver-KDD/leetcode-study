class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ### method 1
        # arr.sort(key=lambda i:abs(i-x))
        # return sorted(arr[:k])
        
        ### method 2 (heap)
#         arr.sort(key=lambda i:abs(i-x))
#         heap = []
#         for i in range(k):
#             heapq.heappush(heap, arr[i])
#         return sorted(heap)
    
        ### method 3 (binary search)
        left, right = 0, len(arr)-1
        while left < right:
            mid = (left+right)//2
            if arr[mid] < x:
                left = mid+1
            else:
                right = mid

        left -= 1
        if left == -1:
            return arr[:k]
        elif left == len(arr)-1:
            return arr[-k:]
        else:
            res = []
            while len(res) < k:
                if left == -1:
                    res.append(arr[right])
                    right += 1
                elif right == len(arr):
                    res.append(arr[left])
                    left -= 1
                else:
                    if abs(arr[left]-x) <= abs(arr[right]-x):
                        res.append(arr[left])
                        left -= 1
                    else:
                        res.append(arr[right])
                        right += 1
            return sorted(res)