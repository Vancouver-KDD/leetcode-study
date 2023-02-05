var threeSum = function(nums) {
   const result = [];
   nums = nums.sort((a,b) => a-b)

   for(let i=0; i< nums.length -2; i++) {
      if(i>0 && nums[i] === nums[i-1]) continue;

    let left = i +1;
    let right = nums.length -1;

    while(left<right) {
      const sum = nums[i] + nums[left] + nums[right]
      if(sum<0) {
         left++;
      } else if(sum >0) {
         right--;
      } else {
         result.push([nums[i], nums[left], nums[right]])
      }
    }
}
   return result;
};

console.log(threeSum())