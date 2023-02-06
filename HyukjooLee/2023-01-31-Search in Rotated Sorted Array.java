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
// Step 1. create pointers indicating start and end of the array
// Step 2. if one of two pointer is pointing to the target element, return that pointer
// otherwise, create another pointer and point it to the middle of them
// Step 3. and again I will check if the new middle pointer is pointing the target
// Step 4. finding the sorted portion of the array and check where the target is, upper limit or lower limit
// Step 5. if target is upper or lower limit, all steps will be processed for that portion
// if not, repeat all steps for the other portion
// time complexity is O(logN) as the size of the subarray being considered is halved.
public int search(int[] nums, int target) {
		// Step 1
		int start = 0;
		int end = nums.length - 1;

		while (start < end) {
			// Step 2
			if (nums[start] == target)
				return start;
			if (nums[end] == target)
				return end;
			int mid = (start + end) / 2;
			// Step 3
			if (nums[mid] == target)
				return mid;
			// Step 4 => Step 5
			// check if the start pointer is smaller than middle point,
			if (nums[start] < nums[mid]) {
				// case 1: target is greater than nums[start] and less than nums[mid], we update the end pointer to mid - 1
			    // nums = [4, 5, 6, 7, 0, 1, 2], target = 5
				// and target value is bigger than start pointer 
				if (target > nums[start] && target < nums[mid])
					end = mid - 1;
				else
			    // case 2: target is smaller than num[start] and greater than nums[mid], 
				// nums = [4, 5, 6, 7, 0, 1, 2], target = 1
				// target is greater than nums[mid] and less than or equal to nums[end], we update the start pointer to mid + 1
					start = mid + 1;
			} else {
				if (target < nums[end] && target > nums[mid])
					start = mid + 1;
				else
					end = mid - 1;
			}
		}
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