// Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

// [4,5,6,7,0,1,2] if it was rotated 4 times.
// [0,1,2,4,5,6,7] if it was rotated 7 times.
// Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

//* Given the sorted rotated array nums of unique elements, return the minimum element of this array.

//Todo: You must write an algorithm that runs in O(log n) time. --> binary search

//* Example 1:

// Input: nums = [3,4,5,1,2]
// Output: 1
// Explanation: The original array was [1,2,3,4,5] rotated 3 times.

const findMin = function (nums) {
  // [3,4,5,1,2]
  let result = nums[0]; // 3
  let l = 0;
  let r = nums.length - 1;
  while (l <= r) {
    if (nums[l] < nums[r]) {
      // 오름차순 정렬 상태
      result = Math.min(result, nums[l]);
      break;
    }
    let m = Math.floor((l + r) / 2); // 2
    result = Math.min(result, nums[m]); // min(3,nums[2]=5)=3
    if (nums[m] >= nums[l]) {
      // 5 >= 3 True
      l = m + 1; // 3번 인덱스 [3,4,5,((1)),2]
    } else {
      r = m - 1;
    }
  }
  return result;
};
