// Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

// Example 1:
// Input: nums = [1,1,1,2,2,3], k = 2
// Output: [1,2]

// Example 2:
// Input: nums = [1], k = 1
// Output: [1]

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
  const seen = {};

  for (let num of nums){
      if(seen[num] === undefined){
          seen[num] = 1
      } else {
          seen[num]++
      }
  }

  const bucket = [];
  for(let i=0; i<=nums.length; i++){
      bucket.push([])
  }

  for(let key in seen){
      let count = seen[key]
      bucket[count].push(key)
  }
  
  let result = [];
  for(let i=bucket.length-1; i>=0; i--){
      if(bucket[i].length === 0){
          continue
      } else {
          result = [...result, ...bucket[i]]
      }
  }
  return result.splice(0, k)
};