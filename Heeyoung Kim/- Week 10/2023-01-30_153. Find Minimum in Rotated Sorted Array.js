// 153. Find Minimum in Rotated Sorted Array

// Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

// [4,5,6,7,0,1,2] if it was rotated 4 times.
// [0,1,2,4,5,6,7] if it was rotated 7 times.
// Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

// Given the sorted rotated array nums of unique elements, return the minimum element of this array.

// You must write an algorithm that runs in O(log n) time.

 

// Example 1:

// Input: nums = [3,4,5,1,2]
// Output: 1
// Explanation: The original array was [1,2,3,4,5] rotated 3 times.


var findMin = (nums) => {
    let left = 0, right = nums.lenght-1;

    if(nums.length === 1) return nums[0];
    if(nums[left] < nums[right]) return nums[left];

    while(left <= right) {
        const mid = Math.floor((left+right) / 2);
        let leftval = nums[left] , midval = nums[mid] , leftofMid = nums[mid-1], rightofMid = nums[mid+1];

        if(midval > rightofMid) return rightofMid;
        else if(leftofMid > midval) return midval;

        if(leftval < midval) left = mid+1;
        else if(leftval > midval) right = mid-1;
    }
}

//Time Complexity : O(log N)