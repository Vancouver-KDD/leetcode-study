// There is an integer array nums sorted in ascending order (with distinct values).
// Given the array nums after the possible rotation and an integer target,
// return the index of target if it is in nums, or -1 if it is not in nums.
// You must write an algorithm with O(log n) runtime complexity.

// 1. using two pointers
// this problem is searching the target in the given array
// but array is rotated at some index
// [4,5,6,7,0,1,2]
// this array is rotated at index 3 and target value is positioned at index 4 after rotation
// if the value is not present in the given array, we return -1
// otherwise return the target value index

// 1. finding the target in the sorted and rotated array nums
// the fact is that one side of the array is always sorted in ascending order 
// and uses it to determine the direction of the search

// Review
// 문제를 시작하기 전에 time complexity limitation 확인
// if there is no limit, linear search can be introduced first
// 이 문제는 rotated 된 array 에서 타겟을 찾는 문제
// 주어진 타겟이 어레이 안에 있으면 타겟의 인덱스를 리턴
// 없으면 -1 를 리턴

// 메인 아이디어는 타겟은 정렬된 어레이 포션 안에 있다는 가정을 함으로써
// 바이너리 서치를 사용하여 타겟을 찾는것에 목적을 준다
// 정렬되기 위해서는 L <= R 가 성립이 되야함

// 주어진 인풋 어레이 안에서 right portion 이 sorted 되기 위해서는 L <= mid
// check if the target is within the sorted left side 
// target >= nums[left] && target < nums[mid]
// if true, right = mid - 1 
// if false, left = mid + 1
// 2. 반대로 right portion 이 sorted 되기 위해서는 mid <= R
// check if the target is within the sorted right side
// target > nums[mid] && target <= nums[right]
// if true, left = mid + 1
// if false, right = mid - 1 

// at the end of loop, we will find the target
// otherwise, return - 1
public int search(int[] nums, int target) {
		int left = 0;
		int right = nums.length - 1;

		// continue the loop until the search space is exhausted
		while (left <= right) {
			int mid = (left + right) / 2;

			// check if the target is at the middle index
			if (nums[mid] == target) {
				return mid;
			}

			// check if the left side of the array is sorted
			if (nums[left] <= nums[mid]) {
				// Check if the target is within the sorted left side
				if (target >= nums[left] && target < nums[mid]) {
					right = mid - 1;
				} else {
					left = mid + 1;
				}
			}
			// check if the right side of the array is sorted
			// [6,0,1,2,3,4,5]
			else {
				// check if the target is within the sorted right side
				if (target > nums[mid] && target <= nums[right]) {
					left = mid + 1;
				} else {
					right = mid - 1;
				}
			}
		}
		// return -1 if the target is not found
		return -1;
}

// 2. using linear search
// time complexity is O(N)
public int search(int[] nums, int target) {
    for (int i = 0; i < nums.length; i++) {
        if (nums[i] == target) {
            return i;
        }
    }
    return -1;
}