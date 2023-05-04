var twoSum = function(nums, target) {
    // check if parameters are valid
    if (!nums || !target || nums.length < 2 || target < 0) {
        return [0, 0]
    }

    // loop through nums and compare one item with rest of the items in the array
    for (let i = 0; i < nums.length; i++) {
        for (let j = i+1; j < nums.length; j++) {
            if (nums[i] + nums[j] === target) {
                return [i, j]
            }
        }
    }

    // complexity
    // time: O(n^2) // double for loop
    // space: O(1) // no variable made (only for for loop)
};

// Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
var twoSum2 = function(nums, target) {
    // check if parameters are valid
    if (!nums || !target || nums.length < 2 || target < 0) {
        return [0, 0]
    }

    // going to loop through every item in the nums list and save the possiple pair number
    // and check if the next number in the list is in the possiple pair
    const diffList = {}
    for (let i = 0; i < nums.length; i++) {
		let diff = target - nums[i]
        if (diffList[diff] !== undefined) {
            return [diffList[diff], i]
        }
        diffList[nums[i]] = i;
    }
    
    // complexity
    // time: O(n) // linear loop
    // space: O(n) // making list of possiple number
};