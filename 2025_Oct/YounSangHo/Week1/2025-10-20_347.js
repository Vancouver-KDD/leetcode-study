/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  const freq = new Map();
  for (let num of nums) {
    freq.set(num, (freq.get(num) || 0) + 1);
  }

  const buckets = Array(nums.length + 1)
    .fill()
    .map(() => []);
  for (let [num, count] of freq.entries()) {
    buckets[count].push(num);
  }

  const res = [];
  for (let i = buckets.length - 1; i >= 0 && res.length < k; i--) {
    for (let num of buckets[i]) {
      res.push(num);
      if (res.length === k) return res;
    }
  }
  return res;
};
