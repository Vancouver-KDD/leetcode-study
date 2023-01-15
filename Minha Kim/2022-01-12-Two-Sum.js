/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

// Solution 1 

const twoSum = function(nums, target) {
  for(let i=0; i<nums.length; i++){
      for(let j=i+1; j<nums.length; j++){
          if(nums[i] + nums[j] === target){
              return [i, j]
          }
      }
  }
};

// Solution 2 

const twoSum = function (nums, target) {
  const map = {};
  for (let i = 0; i < nums.length; i++) {
      let value = nums[i];
      let complementPair = target - value;
      if(map[complementPair] !== undefined){
          return [map[complementPair], i]
      }
      map[value] = i;
  }
};