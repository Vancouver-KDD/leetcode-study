// Only need to check if there’s duplicate
// JavaScript Set Object does not take duplicated items
// so create new Set from the provided array
// and compare the length of array
// and set to check if any duplicated items go ignored by set

var containsDuplicate = function(nums) {
    // check if int array is empty or doesn't exist
    if (!nums || !nums.length) {
        return false
    }
    // create new Set -> eliminate duplates if exist
    const numsSet = new Set(nums)
    // compare given array and new set length
    return nums.length == numsSet.size ? false : true
};