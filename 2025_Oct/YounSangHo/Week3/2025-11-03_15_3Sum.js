/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  // integer array
  // [i,j,k]그룹을 만들어서 그 값이 0이 되도록 그리고 i,j,k는 모두 다르다
  // i,j,k 모두 다른 값
  // i,j가 정해지면 k값이 정해진다.
  const res = [];
  // Sort the array numerically
  nums.sort((a, b) => a - b);
  const n = nums.length;

  for (let i = 0; i < n - 2; i++) {
    // Skip duplicate values for the first element
    if (i > 0 && nums[i] === nums[i - 1]) {
      continue;
    }

    let j = i + 1; // Left pointer
    let k = n - 1; // Right pointer

    while (j < k) {
      const total = nums[i] + nums[j] + nums[k];

      if (total > 0) {
        // Sum is too large
        k--;
      } else if (total < 0) {
        // Sum is too small
        j++;
      } else {
        // Found a triplet
        res.push([nums[i], nums[j], nums[k]]);
        j++;

        // Skip duplicate values for the second element
        while (j < k && nums[j] === nums[j - 1]) {
          j++;
        }
      }
    }
  }
  return res;
};
