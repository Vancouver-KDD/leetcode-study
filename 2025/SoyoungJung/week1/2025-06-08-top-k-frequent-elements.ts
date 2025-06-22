function topKFrequent(nums: number[], k: number): number[] {
  const lookup: { [key: number]: number } = {};

  for (const num of nums) {
    lookup[num] = (lookup[num] || 0) + 1;
  }

  const result = Object.entries(lookup)
    .sort((a, b) => b[1] - a[1])
    .slice(0, k)
    .map((item) => Number(item[0]));

  return result;
}
