var twoSum = function(nums, target) {
    //boundary check
    if(nums.length < 2)
        return false;
    let mnums = new Map();
    /*  Logic: equation for question is target = num1 + num2
        equals to num1 = target - num2

        Now searching for num1
        store num2's [key, values] into Map Object
        apply the equation every number by iterating
        until finds num2
    */

    for(let i in nums){
        let y = target - nums[i];
        if(mnums.has(y))
            return [ i, mnums.get(y)]
        mnums.set(nums[i],i)
    }
    return null

};