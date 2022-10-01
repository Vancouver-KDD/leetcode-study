class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # O(log n)의 시간복잡도를 갖기 위해서는 매 연산마다 앞으로의 연산수가 반으로 줄어야 한다
        # 정렬되어있는 배열이기 때문에, middle값과 right값의 크기 비교를 통해 최소값이 middle값의 좌우 어디에 있을지 예측할수 있다

        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            # 가운데수 뒤로 오름차순인경우(최소값이 middle이하의 인덱스에 있다)
            if nums[middle] < nums[right]:
                right = middle

            # 가운데수 뒤로 오름차순이 아닌 경우(최소값이 middle 초과의 인덱스에 있다)
            elif nums[middle] > nums[right]:
                left = middle + 1
        return nums[left]