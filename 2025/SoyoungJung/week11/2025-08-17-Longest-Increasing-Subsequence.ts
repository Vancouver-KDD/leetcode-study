function lengthOfLIS(nums: number[]): number {
  const sub: number[] = [];

  for (const num of nums) {
    let left = 0,
      right = sub.length - 1;

    while (left <= right) {
      const mid = Math.floor((left + right) / 2);
      if (sub[mid] < num) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }

    if (left < sub.length) {
      sub[left] = num;
    } else {
      sub.push(num);
    }
  }

  return sub.length;
}
