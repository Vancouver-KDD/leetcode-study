const containsDuplicate = (nums) => {
  const set = new Set(nums)
  if (set.size === nums.length) {
    return false
  } else {
    return true
  }
}

containsDuplicate([1,2,3,1])
