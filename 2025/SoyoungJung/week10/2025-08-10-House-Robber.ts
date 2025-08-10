function rob(nums: number[]): number {
  if (nums.length === 0) return 0;
  if (nums.length === 1) return nums[0];

  let prev2 = nums[0];
  let prev1 = Math.max(nums[0], nums[1]);

  for (let i = 2; i < nums.length; i++) {
    const temp = prev1;
    prev1 = Math.max(prev1, prev2 + nums[i]);
    prev2 = temp;
  }
  return prev1;
}
