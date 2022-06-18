// There is an integer array nums sorted in ascending order (with distinct values).

// [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

// Given the array nums after the possible rotation and an integer target,
//Todo: return the index of target if it is in nums, or -1 if it is not in nums.

//Todo: You must write an algorithm with O(log n) runtime complexity. --> binary search

//* Example 1:

// Input: nums = [4,5,6,7,0,1,2], target = 0
// Output: 4

//* Example 2:

// Input: nums = [4,5,6,7,0,1,2], target = 3
// Output: -1

const search = function (nums, target) {
  let l = 0;
  let r = nums.length - 1;

  while (l < r) {
    const m = Math.floor((l + r) / 2);
    if (nums[m] == target) return m;

    if (nums[l] <= nums[m]) {
      // 왼쪽 반 오름차순 정렬 상태  --> [4,5,6,((7)),0,1,2], target = 5
      if (target >= nums[l] && target < nums[m]) {
        // target이 왼쪽반에 속하면 r을 middle pointer로 옮겨 오른쪽 반을 버린다.
        r = m;
      } else {
        l = m + 1;
      }
    } else {
      // 오른쪽 반 오름차순 정렬 상태 --> [5,6,0,((1)),2,3,4], target = 7
      if (target > nums[m] && target <= nums[r]) {
        l = m + 1;
      }
      // Number is in the left side
      else {
        r = m; // l=0, m3 [5,((6)),0,1] --> [0,1]
      }
    }
  }

  // Reached the final number; return it if it matches the target, else target was not found
  return nums[l] === target ? l : -1;
};
