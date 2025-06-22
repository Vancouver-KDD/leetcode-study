class Solution {
  /**
   * @param {number[]} nums
   * @param {number} k
   * @return {number[]}
   */
  topKFrequent(nums, k) {
    const frequentMap = new Map();
    const result = [];

    nums.forEach((num) => {
      if (frequentMap.has(num)) {
        frequentMap.set(num, frequentMap.get(num) + 1);
      } else {
        frequentMap.set(num, 1);
      }
    });

    const sortedArray = Array.from(frequentMap).sort((a, b) => b[1] - a[1]);

    for (let i = 0; i < k; i++) {
      result.push(sortedArray[i][0]);
    }

    return result;
  }
}
