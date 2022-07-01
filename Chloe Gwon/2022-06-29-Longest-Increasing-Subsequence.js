var lengthOfLIS = function(nums) {
    var dp = new Array(nums.length).fill(1);
    var maxLength = 0;
    
    for (var i=nums.length-1; i>=0; i--){
        for (var j=i+1; j<nums.length; j++){
            if (nums[i]<nums[j] && dp[i]<dp[j]+1){
                dp[i] = dp[j]+1;
            }
        }
        maxLength = Math.max(maxLength, dp[i]);
    }
    
    return maxLength;
};

/*
example DP values:
0 1 0 3 2 3
          1
        2
      1
    3
  3
4
*/
