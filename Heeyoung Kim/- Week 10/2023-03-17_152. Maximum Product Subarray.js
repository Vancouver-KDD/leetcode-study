const maxProduct = (nums) => {
    let max = [nums[0]];
    let min = [nums[0]];
    let maxresult = nums[0];

    for(let i=0; i<nums.length; i++) {
        max[i] = Math.max(nums[i], nums[i] * max[i-1], nums[i] * min[i-1]); //가장 곱이 큰 값들 끼리의 더 큰 값을 max에 push 한다. (minimum 값을 여기에서 사용해서 가장 큰 값을 넣어주기 때문에 음수 걱정 무! )
        min[i] = Math.min(nums[i], nums[i] * max[i-1], nums[i] * min[i-1]); //가장 곱이 작은 값들 끼리의 더 작은 값을 min 에 push 한다. 
        maxresult = Math.max(maxresult, max[i]);
    }

    return maxresult;
}