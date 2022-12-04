//내가 한것
const search = (nums, target) => {
  let MapTable = new Map()
  for (let a = 0; a < nums.length; a++) {
    MapTable.set(nums[a], a)
  }
  if (MapTable.has(target)) {
    return MapTable.get(target)
  } else {
    return -1
  }
}
console.log(search([4, 5, 6, 7, 0, 1, 2], 4))

const search = (nums, target) => {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    let mid = Math.floor(left + (right - left) / 2)
    if (nums[mid] === target) return mid;
    if (nums[left] <= nums[mid]) {
      if (nums[left] <= target && target < nums[mid]) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    } else {
      if (nums[mid] < target && target <= nums[right]) {
        left = mid + 1
      } else {
        right = mid - 1
      }
    }
  }

  return -1
}

