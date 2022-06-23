function search(nums) {
  left = 0; 
  right = nums.length - 1;

  while(left <= right) {
    let mid = Math.floor((left + right) /2);

    if(nums[mid] === target) return mid;

    if(nums[left] <= nums[mid]) {
      if(nums[left] <= target && target <= nums[mid])
        right = mid - 1;   // L T M 
        else left = mid + 1;       // L M T
    } else {
      if(nums[mid] <= target && target <= nums[right]) 
        left = mid + 1;    // M T R
        else right = mid - 1;       // T M R
    }
  }
  return -1; 
}