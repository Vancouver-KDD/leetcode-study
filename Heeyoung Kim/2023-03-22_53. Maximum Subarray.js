let maxSumArray = (nums) => {
    let localmax = nums[0];
    let globalmax = nums[0];

    for(let i=0; i<nums.length; i++) {
        localmax = Math.max(nums[i], localmax + nums[i]);
        if(localmax > globalmax) {
            globalmax = localmax;
        }
    }

    return globalmax;
}