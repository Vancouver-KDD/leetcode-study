from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0 
        end = len(nums) - 1

        while start < end:
            mid = (start + end) // 2
            
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                 end = mid
                
        return nums[start]

'''
It maintains two pointers, start and end, which converge towards the minimum element.
It compares the element at the mid with the element at the end pointer.
If nums[mid] > nums[end], it means the minimum must be to the end of mid, so it updates the start pointer to mid + 1.
If nums[mid] <= nums[end], it means the minimum must be at mid or to its start, so it updates the end pointer to mid.

설명
레프트와 라이트 포인터를 이용한다.
주의해야할 점은, 만약에 미드 포인트가 엔드포인트보다 크다면 가장 작은 값은 미드포인트 이후에 있다. 
왜냐하면 해당 미드~엔드 어레이가 오름차순으로 정렬되어있지 않다는 의미이기 때문이다. 
이는 곧 전체 어레이 자체가 오름차순으로 정렬이 되어있는 어레이가 아님을 의미한다. 
따라서 가장 작은 값은 오름차순으로 계속 올라가다가 갑자기 패턴이 깨지는 곳에 있다. 

만약에 미드포인트가 엔드포인트보다 작다면 
이는 곳 미드~엔드까지는 오름차순으로 정리되어있다는 이야기이이다. 따라서 미드 이전을 탐색한다. 
미드 이전이 여전히 오름차순이라면 인덱스 0을 리턴할 것이다. 아니라면 위의 로직을 이용해 범위를 줄인다. 
'''

'''
if mid to end is increasing:
    then focus on other half
else:
    move start pointer
'''