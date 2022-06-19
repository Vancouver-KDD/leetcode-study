var threeSum = function(nums) {
    const result = [];
    nums.sort((a,b) => a-b);

    for (var i=0; i<nums.length-2; i++){
        if (i>0 && (nums[i] === nums[i-1])) continue;
        var left = i+1;
        var right = nums.length-1;
    
        while (left < right){
            var threeSum = nums[i] + nums[left] + nums[right];
            if (threeSum > 0){
                right--;
            } else if (threeSum < 0){
                left++;
            } else{
                result.push([nums[i], nums[left], nums[right]]);
                
                while(nums[left] === nums[left+1]){
                    left++;
                }
                // while(nums[right] === nums[right-1]){
                //     right--;
                // }
                left++;
                // right--;
            }
        }
    }
    
    return result;
};
