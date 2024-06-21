/**
 * @param {number[]} fruits
 * @return {number}
 */
var totalFruit = function (fruits) {
  if (new Set(fruits).size < 3) return fruits.length

  let sameType = 0
  let max = 0

  for (let i = 0; i < fruits.length; i++) {
    if (fruits[i] === fruits[i + 1]) {
      sameType++
      continue
    }

    const set = new Set()
    for (let j = i; j < fruits.length; j++) {
      set.add(fruits[j])
      if (set.size === 2) max = Math.max(max, j - i + 1 + sameType)
      if (set.size > 2) break
    }
    sameType = 0
  }
  return max
}

let fruits = [1, 2, 3, 2, 2]
console.log(totalFruit(fruits))
