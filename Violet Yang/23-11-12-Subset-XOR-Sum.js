var subsetXORSum = function(nums) {
    let sum=0;
    dfs(0, 0); return sum;
    
    function dfs(val, i){
        if(i<nums.length){
            dfs(val^nums[i], i+1);  // to XOR with nums[i].
            dfs(val, i+1);          // NOT to XOR.
        }
        if(i==nums.length){sum+=val};
    }
};