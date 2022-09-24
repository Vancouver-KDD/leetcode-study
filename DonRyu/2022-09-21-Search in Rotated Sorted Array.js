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
