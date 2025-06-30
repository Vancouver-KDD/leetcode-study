function binarySearch(nums: number[], target: number): number {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    const guess = nums[mid];

    if (guess === target) {
      return mid;
    } else if (guess < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return -1;
}
