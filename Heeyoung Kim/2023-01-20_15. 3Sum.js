// Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
// Notice that the solution set must not contain duplicate triplets.

// Example 1:
// Input: nums = [-1,0,1,2,-1,-4]
// Output: [[-1,-1,2],[-1,0,1]]
// Explanation: 
// nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
// nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
// nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
// The distinct triplets are [-1,0,1] and [-1,-1,2].
// Notice that the order of the output and the order of the triplets does not matter.

var threeSum = function(nums) {
    nums.sort((a,b) => a-b);
    let result = [];
   
    for(let i=0; i<nums.length; i++) {
      let target = 0 - nums[i];
      let left = i+1;
      let right = nums.length - 1;
      
        if(i > 0 && nums[i] === nums[i-1]) {
          continue;
        }
  
        while(left < right) {
          if(nums[left] + nums[right] === target) {
            result.push([nums[i], nums[left], nums[right]]);
            left++;
            
            while(nums[left] === nums[left-1]) {left++;}
            
          }else if(nums[left] + nums[right] < target) {
            left++;
          }else if(nums[left] + nums[right] > target) {
            right--;
          }
         }
      }
  
      return result;
  }
  threeSum([-1,0,1,2,-1,-4]);
  
  //Time Complexity : O(n) sort 메소드를 사용하는 부분도 O(N) => sort 메소드를 사용안함으로써 Time Complexity를 줄이는 방법은 128번 문제 참고 **
  // Twopointer 를 알고리즘으로 사용하는 부분에도 시간 복잡도는 O(N) 이 된다. start 와 end가 배열의 마지막으로 오는 경우가 있기 때문에
  //Space Complexity : O(n) result 를 사용하는 배열에 space를 사용하기 때문에