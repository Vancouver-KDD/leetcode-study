var containsDuplicate = function(nums) {
    nums = nums.sort() // asending sort => [1,2,3,4]

    for(let i=0; i<nums.length; i++) {
        if(nums[i] == nums[i+1]){
            return true;
        } 
        
    }
    return false;
};

// A JavaScript Set is a collection of unique values. Each value can only occur once in a Set. A Set can hold any value of any data type.

// const numbers = [2,3,4,4,2,3,3,4,4,5,5,6,6,7,5,32,3,4,5]

//spreading numbers of the object into an array using the new operator
// console.log([...new Set(numbers)]) 

// [2, 3, 4, 5, 6, 7, 32]

var containsDuplicate = function(nums) {
    let set = new Set(nums);

    return set.size !== nums.length
};

// time complexity o(n) space complexity o(n)