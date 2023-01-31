// Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
// For example, the array nums = [0,1,2,4,5,6,7] might become:
// Given the sorted rotated array nums of unique elements, return the minimum element of this array.
// You must write an algorithm that runs in O(log n) time.

// 1. using binary search
// rotated sorted array.. some elements moved to the end of the array
// while, some elements moved to the beginning of the array
// so sorted array is not longer exists
// binary search will be a solution for this problem
// time complexity is O(logN) as we dicard the half of the array every times 
public int findMin(int[] nums) {
		// binary search
		int start = 0;
        int end = nums.length - 1;
		while (start < end) {
			// calculate middle index
			int mid = (start + end) / 2;
			// if the middle element of the array is bigger than end element
			if (nums[mid] > nums[end])
				// update start pointer with mid + 1 
                // as the min element will be on the right side of mid
				start = mid + 1;
			else
				// move end pointer as the min element will be on the left side of mid
				end = mid;
		}

		return nums[start]; // or nums[start]
}

// 2. using linear search
// this solution would be not a proper solution as it requires O(logN) time complexitiy
// but it is the simplest solution, time complexity is O(N)
// we iterate through the array from the second element to the last element
// if an element is less than the previous element, we return the element as the min element
// if the loop completes without finding a minimum element, we return the first element as the minimum
public int findMin(int[] nums) {
    for(int i = 1; i < nums.length; i++) {
        if(nums[i] < nums[i -1]) {
            return nums[i];
        }
    }
    return nums[0];
}