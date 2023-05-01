var containsDuplicate = function(nums) {
    let anum = []
    for(let i in nums){
        //spit out true if finds same number in the array
        if(anum.includes(nums[i]))
            return true;
        else
        //seperate non-duplicates
            anum.push(nums[i])
    }
    return false;
};