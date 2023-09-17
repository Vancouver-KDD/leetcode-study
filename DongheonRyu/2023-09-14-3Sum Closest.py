def threeSumClosest(nums, target):
    nums.sort()  # 입력 배열 정렬
    closest_sum = float('inf')  # 가장 가까운 합을 나타내는 변수 초기화

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            diff = abs(current_sum - target)  # 현재 합과 target과의 차이 계산
            
            if diff < abs(closest_sum - target):
                closest_sum = current_sum  # 더 가까운 합이면 업데이트
            
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum  # 정확히 일치하는 경우

    return closest_sum

# 예제 입력
nums1 = [-1, 2, 1, -4]
target1 = 1

nums2 = [0, 0, 0]
target2 = 1

# 결과 출력
print(threeSumClosest(nums1, target1))  # Output: 2
print(threeSumClosest(nums2, target2))  # Output: 0
